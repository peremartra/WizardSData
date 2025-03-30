"""
Basic usage example for WizardSData.
"""
import os
import sys
import json
from dotenv import load_dotenv
TEMPLATE_NAME= "templates/financial_retail_banking/"
# Add parent directory to path to import the library
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import wizardsdata as wsd

def main():
    """Example of using WizardSData."""
    # Load environment variables from config.env
    env_path = os.path.join(os.path.dirname(__file__), '..', 'config.env')
    load_dotenv(env_path)
    
    # Get API key from environment
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("ERROR: OPENAI_API_KEY not found in environment variables. Check your config.env file.")
        return
    
    # Configure the library
    missing = wsd.set_config(
        API_KEY=api_key,  # Use API key from environment variable
        template_client_prompt=TEMPLATE_NAME + "prompts/financial_client_01.j2",
        template_advisor_prompt=TEMPLATE_NAME + "prompts/financial_advisor_01.j2",
        file_profiles=TEMPLATE_NAME + "profiles/retail_banking_5.json",
        file_output=TEMPLATE_NAME + "outputs/test_dataset01_5b.json",
        model_client="gpt-4o",
        model_advisor="gpt-4o",
        # Optional parameters with custom values
        temperature_client=0.8,
        max_recommended_questions=10
    )
    
    # Check for missing parameters
    if missing:
        print(f"Missing configuration parameters: {', '.join(missing)}")
        return
    
    # Display current configuration
    config = wsd.get_config()
    print("Current configuration:")
    # Mask API key for security when printing
    masked_config = {**config, "API_KEY": "********" if "API_KEY" in config else None}
    print(json.dumps(masked_config, indent=2))
    
    # Check if configuration is valid
    if not wsd.is_config_valid():
        print("Configuration is not valid.")
        return
    
    # Start generating conversations
    print("Starting conversation generation...")
    success = wsd.start_generation()
    
    if success:
        print("Conversations generated successfully!")
    else:
        print("Failed to generate conversations.")


if __name__ == "__main__":
    main()