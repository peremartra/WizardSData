"""
Create a Retail Banking Conversation Dataset
===========================================

This module demonstrates how to use the WizardSData library to generate
synthetic conversational datasets for retail banking scenarios.

Example:
    To run this script directly::

        $ python create_dataset.py

Notes:
    - Requires an OPENAI_API_KEY in config.env
    - Uses the financial retail banking templates
    - Creates a dataset based on the retail_banking_160.json profiles
"""
import os
import sys
import json
from dotenv import load_dotenv

# Define the template directory
TEMPLATE_NAME = "templates/financial_retail_banking/"

# Explicitly point to the project root for importing wizardsdata
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.insert(0, PROJECT_ROOT)

# Now import the library - this will use the latest version
import wizardsdata as wsd

def main():
    """
    Generate a retail banking conversation dataset using WizardSData.
    
    This function demonstrates the complete workflow from configuration to generation
    of financial conversations between clients and advisors.
    
    Steps:
        1. Load API credentials from environment
        2. Configure the WizardSData library
        3. Validate the configuration
        4. Generate conversations
        5. Report results
        
    Returns:
        None
    
    Raises:
        EnvironmentError: If the OPENAI_API_KEY is not found in environment variables
    """
    # Load environment variables from config.env
    env_path = os.path.join(os.path.dirname(__file__), '../..', 'config.env')
    load_dotenv(env_path)
    
    # Get API key from environment
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("ERROR: OPENAI_API_KEY not found in environment variables. Check your config.env file.")
        return
    
    # Configure the library with required parameters
    missing = wsd.set_config(
        # Authentication settings
        API_KEY=api_key,  
        
        # Template paths define conversation behavior
        template_client_prompt=TEMPLATE_NAME + "prompts/financial_client_01.j2",
        template_advisor_prompt=TEMPLATE_NAME + "prompts/financial_advisor_01.j2",
        
        # Input/Output file paths
        file_profiles=TEMPLATE_NAME + "profiles/retail_banking_160.json",
        file_output=TEMPLATE_NAME + "outputs/retail_banking_dataset_b.json",
        
        # Model configuration
        model_client="gpt-4o",
        model_advisor="gpt-4o",
        
        # Conversation parameters
        temperature_client=0.6,
        temperature_advisor=0.2,
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