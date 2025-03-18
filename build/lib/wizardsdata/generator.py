"""
Conversation generator for WizardSData.
"""
import os
import json
import uuid
from typing import Dict, Any, List, Optional
import openai

from .config import config
from .templates import render_prompt_from_path


def initialize_apis(api_key: Optional[str] = None) -> tuple:
    """
    Initialize API clients for OpenAI.
    
    Args:
        api_key: Optional API key to use. If None, uses the one from config.
        
    Returns:
        Tuple with (client_api, advisor_api)
    """
    key = api_key or config.get('API_KEY')
    if not key:
        raise ValueError("API_KEY is required but not provided")
    
    client_api = openai.Client(api_key=key)
    advisor_api = openai.Client(api_key=key)
    
    return client_api, advisor_api


def get_model_response(api_client, model: str, messages: List[Dict[str, str]], 
                       temperature: float, top_p: float, frequency_penalty: float, 
                       max_tokens: Optional[int]) -> str:
    """
    Get response from a model using the OpenAI API.
    
    Args:
        api_client: OpenAI client instance.
        model: Model name to use.
        messages: List of message dictionaries (role and content).
        temperature: Temperature setting for response randomness.
        top_p: Top p setting for response diversity.
        frequency_penalty: Frequency penalty to apply.
        max_tokens: Maximum number of tokens to generate.
        
    Returns:
        The generated response as a string.
    """
    params = {
        'model': model,
        'messages': messages
    }
    
    # Add optional parameters if provided
    if temperature is not None:
        params['temperature'] = temperature
    if top_p is not None:
        params['top_p'] = top_p
    if frequency_penalty is not None:
        params['frequency_penalty'] = frequency_penalty
    if max_tokens is not None:
        params['max_tokens'] = max_tokens
    
    response = api_client.chat.completions.create(**params)
    return response.choices[0].message.content.strip()


def initiate_conversation(client_prompt: str, advisor_prompt: str, financial_goal: str, 
                          client_api, advisor_api, max_questions: int) -> List[Dict[str, Any]]:
    """
    Initiate a continuous conversation between client and advisor models.
    
    Args:
        client_prompt: System prompt for the client model.
        advisor_prompt: System prompt for the advisor model.
        financial_goal: Financial goal for this conversation.
        client_api: OpenAI client for the client model.
        advisor_api: OpenAI client for the advisor model.
        max_questions: Maximum number of interactions.
        
    Returns:
        List of dictionaries representing the conversation.
    """
    # Get configuration parameters
    model_client = config.get('model_client')
    temperature_client = config.get('temperature_client')
    top_p_client = config.get('top_p_client')
    frequency_penalty_client = config.get('frequency_penalty_client')
    max_tokens_client = config.get('max_tokens_client')
    
    model_advisor = config.get('model_advisor')
    temperature_advisor = config.get('temperature_advisor')
    top_p_advisor = config.get('top_p_advisor')
    frequency_penalty_advisor = config.get('frequency_penalty_advisor')
    max_tokens_advisor = config.get('max_tokens_advisor')
    
    # Generate unique conversation ID
    conversation_id = str(uuid.uuid4())
    conversation_dataset = []
    sequence = 0

    # Initialize conversations with system prompts
    client_conversation = [{"role": "system", "content": client_prompt}]
    advisor_conversation = [{"role": "system", "content": advisor_prompt}]

    for _ in range(round(max_questions * 2.1)):
        # Client response
        client_response = get_model_response(
            client_api, 
            model=model_client, 
            messages=client_conversation, 
            temperature=temperature_client, 
            top_p=top_p_client,
            frequency_penalty=frequency_penalty_client,
            max_tokens=max_tokens_client
        )
        print("client: " + client_response)
        
        # Add the client response to the dataset BEFORE checking for [END]
        conversation_dataset.append({
            "id_conversation": conversation_id,
            "topic": financial_goal,
            "sequence": sequence,
            "input": client_conversation[-1]['content'] if len(client_conversation) > 1 and client_conversation[-1]['role'] == 'user' else "Start conversation",
            "output": client_response.replace("[END]", "").strip()
        })
        
        # Now check for [END] after adding to dataset
        if "[END]" in client_response:
            break
            
        client_conversation.append({"role": "assistant", "content": client_response})
        advisor_conversation.append({"role": "user", "content": client_response})
        sequence += 1

        # Advisor response
        advisor_response = get_model_response(
            advisor_api, 
            model=model_advisor, 
            messages=advisor_conversation, 
            temperature=temperature_advisor,
            top_p=top_p_advisor,
            frequency_penalty=frequency_penalty_advisor,
            max_tokens=max_tokens_advisor
        )
        print("advisor: " + advisor_response)
        
        # Add the advisor response to the dataset BEFORE checking for [END]
        conversation_dataset.append({
            "id_conversation": conversation_id,
            "topic": financial_goal,
            "sequence": sequence,
            "input": advisor_conversation[-1]['content'],
            "output": advisor_response.replace("[END]", "").strip()
        })
        
        # Now check for [END] after adding to dataset
        if "[END]" in advisor_response:
            break
            
        advisor_conversation.append({"role": "assistant", "content": advisor_response})
        client_conversation.append({"role": "user", "content": advisor_response})
        sequence += 1
    
    return conversation_dataset


def save_conversation(conversations: List[Dict[str, Any]], file_path: str) -> bool:
    """
    Save the conversation dataset to a JSON file.
    
    Args:
        conversations: List of conversation dictionaries.
        file_path: Path to save the conversations.
        
    Returns:
        True if successful, False otherwise.
    """
    try:
        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        
        with open(file_path, 'w') as file:
            json.dump(conversations, file, indent=4)
        return True
    except Exception as e:
        print(f"Error saving conversations: {str(e)}")
        return False


def start_generation() -> bool:
    """
    Start generating conversations between clients and advisors based on the current configuration.
    
    This function orchestrates the entire conversation generation process. It:
    1. Validates the current configuration
    2. Initializes the API clients
    3. Loads conversation profiles from the configured file
    4. Renders prompts for each profile
    5. Generates conversations for each profile using the appropriate models
    6. Saves all conversations to the configured output file
    
    The function relies on the global configuration instance having all necessary
    parameters properly set.
    
    Returns
    -------
    bool
        True if the generation process completed successfully, False otherwise.
        Returns False in the following cases:
        - Invalid configuration (missing parameters)
        - No profiles found in the profile file
        - Failure to render prompts
        - Error during API calls
        - Failure to save conversations
    
    Notes
    -----
    Before calling this function, ensure all required configuration parameters are set:
    - API_KEY: Required for API access
    - template_client_prompt: Path to client prompt template
    - template_advisor_prompt: Path to advisor prompt template
    - file_profiles: Path to JSON file containing conversation profiles
    - file_output: Path where generated conversations will be saved
    - model_client: Model configuration for client responses
    - model_advisor: Model configuration for advisor responses
    
    The function will log progress and error information to standard output.
    
    Examples
    --------
    >>> from wizardsdata.config import set_config
    >>> from wizardsdata.generator import start_generation
    >>> 
    >>> # Set up configuration
    >>> errors = set_config(
    ...     API_KEY="your-api-key",
    ...     template_client_prompt="templates/client.txt",
    ...     template_advisor_prompt="templates/advisor.txt",
    ...     file_profiles="data/profiles.json",
    ...     file_output="output/conversations.json",
    ...     model_client="gpt-4",
    ...     model_advisor="gpt-4"
    ... )
    >>> 
    >>> if not errors:
    ...     # Start generation
    ...     success = start_generation()
    ...     if success:
    ...         print("Generation completed successfully!")
    ...     else:
    ...         print("Generation failed.")
    ... else:
    ...     print(f"Invalid configuration: {errors}")
    """
    # Validate configuration
    if not config.is_valid():
        missing = config.validate()
        print(f"Missing or invalid configuration parameters: {', '.join(missing)}")
        return False
    
    try:
        # Initialize APIs
        client_api, advisor_api = initialize_apis()
        
        # Load profiles
        with open(config.get('file_profiles'), 'r') as file:
            data = json.load(file)
        
        profiles = data.get('profiles', [])
        if not profiles:
            print("No profiles found in the profile file.")
            return False
        
        # Set up prompts for each profile
        prompts = []
        max_recommended_questions = config.get('max_recommended_questions')
        
        for profile in profiles:
            client_prompt = render_prompt_from_path(
                config.get('template_client_prompt'), 
                profile, 
                max_questions=max_recommended_questions
            )
            
            advisor_prompt = render_prompt_from_path(
                config.get('template_advisor_prompt'),
                profile
            )
            
            if not client_prompt or not advisor_prompt:
                print(f"Failed to render prompts for profile {profile.get('id', 'unknown')}")
                continue
            
            prompts.append({
                'profile_id': profile.get('id'),
                'client_prompt': client_prompt,
                'advisor_prompt': advisor_prompt,
                'financial_goal': profile.get('financial_goal', 'Unknown')
            })
        
        # Generate conversations
        all_conversations = []
        for prompt in prompts:
            conversation = initiate_conversation(
                prompt['client_prompt'],
                prompt['advisor_prompt'],
                prompt['financial_goal'],
                client_api,
                advisor_api,
                max_recommended_questions
            )
            
            all_conversations.extend(conversation)
            print(f"Generated conversation for profile {prompt['profile_id']} with {len(conversation)} turns.")
        
        # Save conversations
        success = save_conversation(all_conversations, config.get('file_output'))
        if success:
            print(f"Successfully saved {len(all_conversations)} conversation turns to {config.get('file_output')}")
        else:
            print("Failed to save conversations.")
            return False
        
        return True
    
    except Exception as e:
        print(f"Error during generation: {str(e)}")
        return False