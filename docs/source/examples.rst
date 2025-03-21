Examples
========

This page provides examples of how to use WizardSData in different scenarios.

Basic Usage Example
------------------

Here's a simple example of how to use WizardSData to generate conversations:

.. code-block:: python

   import os
   import sys
   import json
   import wizardsdata as wsd

   def main():
       """Example of using WizardSData."""
       # Configure the library
       missing = wsd.set_config(
           API_KEY="YOUR-API-KEY",  # Replace with your actual API key
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

Loading Configuration from Environment Variables
-----------------------------------------------

You can load the API key from environment variables:

.. code-block:: python

   import os
   import wizardsdata as wsd
   from dotenv import load_dotenv

   # Load environment variables from .env file
   load_dotenv()

   # Get API key from environment
   api_key = os.environ.get("OPENAI_API_KEY")

   # Configure WizardSData with the API key
   errors = wsd.set_config(
       API_KEY=api_key,
       template_client_prompt="templates/client.j2",
       template_advisor_prompt="templates/advisor.j2",
       file_profiles="profiles.json",
       file_output="output.json",
       model_client="gpt-4",
       model_advisor="gpt-4"
   )

   # Check for errors
   if not errors:
       # Start generation
       wsd.start_generation()

Creating and Using a Configuration File
--------------------------------------

You can save and load configuration to/from a file:

.. code-block:: python

   import wizardsdata as wsd

   # Set configuration
   wsd.set_config(
       API_KEY="your-api-key",
       template_client_prompt="templates/client.j2",
       template_advisor_prompt="templates/advisor.j2",
       file_profiles="profiles.json",
       file_output="output.json",
       model_client="gpt-4",
       model_advisor="gpt-4"
   )

   # Save configuration to file
   wsd.save_config("config.json")

   # Later, in another script
   wsd.load_config("config.json")
   wsd.start_generation()

Using the Command Line Interface
-------------------------------

You can use WizardSData from the command line:

.. code-block:: bash

   # Configure WizardSData
   python -m wizardsdata configure \
       --api-key "your-api-key" \
       --client-template "templates/client.j2" \
       --advisor-template "templates/advisor.j2" \
       --profiles "profiles.json" \
       --output "output.json" \
       --client-model "gpt-4" \
       --advisor-model "gpt-4" \
       --config-file "config.json"

   # Generate conversations
   python -m wizardsdata generate

   # Show current configuration
   python -m wizardsdata show-config

   # Load configuration from file
   python -m wizardsdata load-config "config.json"

Creating a Retail Banking Dataset
--------------------------------

Here's an example of creating a retail banking conversation dataset:

.. code-block:: python

   import wizardsdata as wsd
   import json
   import os
   from dotenv import load_dotenv

   # Load API key from environment
   load_dotenv()
   api_key = os.environ.get("OPENAI_API_KEY")

   # Configure WizardSData
   errors = wsd.set_config(
       API_KEY=api_key,
       template_client_prompt="templates/financial01/prompts/financial_client_01.j2",
       template_advisor_prompt="templates/financial01/prompts/financial_advisor_01.j2",
       file_profiles="templates/financial01/profiles/financial_sample01_5.json",
       file_output="test_financial_dataset01_5.json",
       model_client="gpt-4o-mini",
       model_advisor="gpt-4o-mini",
       temperature_client=0.8,
       temperature_advisor=0.1, 
       max_recommended_questions=15
   )

   # Check for errors
   if not errors:
       # Generate conversations
       success = wsd.start_generation()
       if success:
           print("Retail banking dataset generated successfully!")
       else:
           print("Failed to generate retail banking dataset.")
   else:
       print(f"Configuration errors: {errors}")

   # Load and analyze the generated dataset
   with open("test_financial_dataset01_5.json", "r") as f:
       data = json.load(f)
   
   # Print the number of conversation turns
   print(f"Generated {len(data)} conversation turns.")
   
   # Count distinct conversations
   conversations = set(item["id_conversation"] for item in data)
   print(f"Number of distinct conversations: {len(conversations)}")
