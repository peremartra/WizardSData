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
        API_KEY="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",  # Replace with your actual API key
        template_client_prompt="prompts/financial_client_01.j2",
        template_advisor_prompt="prompts/financial_advisor_01.j2",
        file_profiles="profiles/test01_1.json",
        file_output="outputs/test_dataset01.json",
        model_client="gpt-4o-mini",
        model_advisor="gpt-4o-mini",
        # Optional parameters with custom values
        temperature_client=0.8,
        max_recommended_questions=5
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