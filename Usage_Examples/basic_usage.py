"""
Basic usage example for WizardSData.
"""
import os
import sys
import json


# Add parent directory to path to import the library
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import wizardsdata as wsd

def main():
    """Example of using WizardSData."""
    # Configure the library
    missing = wsd.set_config(
<<<<<<< HEAD
        API_KEY="API-KEY",  # Replace with your actual API key
=======
        API_KEY="YOUR-API-KEY",  # Replace with your actual API key
>>>>>>> ee0323e21e5d05ca5c2787a28d907693de1640e6
        template_client_prompt="templates/financial01/prompts/financial_client_01.j2",
        template_advisor_prompt="templates/financial01/prompts/financial_advisor_01.j2",
        file_profiles="templates/financial01/profiles/financial_sample01_1.json",
        file_output="templates/financial01/outputs/test_dataset01_1.json",
        model_client="gpt-4o-mini",
        model_advisor="gpt-4o-mini",
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
    print(json.dumps(config, indent=2))
    
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