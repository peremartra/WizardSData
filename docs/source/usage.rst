Usage Guide
===========

Basic Workflow
-------------

Using WizardSData involves the following steps:

1. Configure the library with required parameters
2. Create prompt templates for different conversation roles
3. Define profiles for the conversation participants
4. Generate conversations
5. Save the conversations to a file

Configuration
------------

First, configure the library with the necessary parameters:

.. code-block:: python

   import wizardsdata as wsd
   
   errors = wsd.set_config(
       API_KEY="your-api-key",
       template_client_prompt="templates/client.txt",
       template_advisor_prompt="templates/advisor.txt",
       file_profiles="profiles.json",
       file_output="conversations.json",
       model_client="gpt-4",
       model_advisor="gpt-4",
       # Optional parameters with custom values
       temperature_client=0.8,
       temperature_advisor=0.5,
       max_recommended_questions=15
   )
   
   if errors:
       print(f"Configuration errors: {errors}")

Required Configuration Parameters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- **API_KEY**: Your OpenAI API key
- **template_client_prompt**: Path to the template file for the client role
- **template_advisor_prompt**: Path to the template file for the advisor role
- **file_profiles**: Path to JSON file containing conversation profiles
- **file_output**: Path where generated conversations will be saved
- **model_client**: Model to use for the client role
- **model_advisor**: Model to use for the advisor role

Optional Configuration Parameters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- **temperature_client**: Temperature for client model sampling (default: 0.7)
- **top_p_client**: Top-p value for client model sampling (default: 0.95)
- **frequency_penalty_client**: Frequency penalty for client model (default: 0.3)
- **max_tokens_client**: Maximum tokens for client responses (default: 175)
- **max_recommended_questions**: Maximum recommended questions (default: 10)
- **temperature_advisor**: Temperature for advisor model sampling (default: 0.5)
- **top_p_advisor**: Top-p value for advisor model sampling (default: 0.9)
- **frequency_penalty_advisor**: Frequency penalty for advisor model (default: 0.1)
- **max_tokens_advisor**: Maximum tokens for advisor responses (default: 325)

Template Structure
-----------------

Templates are used to generate prompts for the conversation participants. They are written in Jinja2 format and can access the profile data:

Example client template (`financial_client_01.j2`):

.. code-block:: text

   You are a {{ profile.age }}-year-old {{ profile.marital_status | lower }} client living in a {{ profile.residence_area | lower }} area of {{ profile.country }}. 
   You work as a {{ profile.profession | lower }} and have {{ profile.financial_knowledge | lower }} financial knowledge. 
   You currently have {{ profile.financial_products | join(' and ') }}. 
   Your main financial goal is to {{ profile.financial_goal | lower }} in the {{ profile.investment_horizon | lower }}. 
   You have a {{ profile.risk_tolerance | lower }} risk tolerance and are looking for advice on how to improve your saving and investment strategy.

   You are having a conversation with a financial advisor.
   - Your first message should be a BRIEF, CASUAL greeting. Don't reveal all your financial details at once.
   - For example, just say hi and mention ONE thing like wanting advice about saving or investments.
   - Keep your first message under 15-30 words. Let the conversation develop naturally.
   - In later messages, respond naturally to the advisor's questions, revealing information gradually.
   - Provide ONLY your next message as the client. Do not simulate the advisor's responses.
   - Start with a natural greeting if this is your first message.
   - Ask relevant questions or express concerns to achieve your goal.
   - Respond naturally and concisely to the advisor's previous message.
   - Try to conclude the conversation in fewer than {{ max_questions }} exchanges.
   - If you feel your questions are resolved, end your message with '[END]'.

Profile Structure
----------------

Profiles define the characteristics of the conversation participants. They are stored in a JSON file:

.. code-block:: json

   {
       "profiles": [
           {
               "id": 1,
               "age": 30,
               "marital_status": "Single",
               "country": "Spain",
               "residence_area": "Urban",
               "profession": "Software Developer",
               "employment_status": "Employed",
               "financial_products": ["Savings account", "Tech stocks"],
               "financial_goal": "Save for house deposit",
               "investment_horizon": "Medium-term",
               "risk_tolerance": "Moderate",
               "financial_knowledge": "Intermediate"
           },
           {
               "id": 2,
               "age": 45,
               "marital_status": "Married",
               "country": "USA",
               "residence_area": "Suburb",
               "profession": "Marketing Manager",
               "employment_status": "Employed",
               "financial_products": ["401k", "Index funds"],
               "financial_goal": "Plan for retirement",
               "investment_horizon": "Long-term",
               "risk_tolerance": "Low",
               "financial_knowledge": "Intermediate"
           }
       ]
   }

Generating Conversations
-----------------------

Once configured, generate conversations with:

.. code-block:: python

   # Check if configuration is valid
   if wsd.is_config_valid():
       # Generate conversations
       success = wsd.start_generation()
       if success:
           print("Conversations generated successfully!")
       else:
           print("Failed to generate conversations.")
   else:
       print("Configuration is not valid.")

Output Format
-----------

Generated conversations are saved as JSON in the following format:

.. code-block:: json

   [
       {
           "id_conversation": "593d41a8-2ee8-47af-a2c8-4d65ddcdf8b6",
           "topic": "Save for house deposit",
           "sequence": 0,
           "rol1": "Hi there! I'm looking for some advice on saving for a house deposit.",
           "rol2": "Hello! I'm glad you reached out for advice on saving for a house deposit. It's an exciting goal! To get started, could you share a bit about your current financial situation? For example, do you have any savings set aside already, and what is your target amount for the deposit?"
       },
       {
           "id_conversation": "593d41a8-2ee8-47af-a2c8-4d65ddcdf8b6",
           "topic": "Save for house deposit",
           "sequence": 2,
           "rol1": "Sure! I have a savings account and some tech stocks, but I'm not sure how much I need for a deposit. Do you have any tips on how to figure that out?",
           "rol2": "Absolutely! The amount you need for a house deposit can vary based on a few factors, such as the property prices in your desired area and the type of mortgage you plan to apply for. Generally, a deposit can range from 10% to 20% of the property's value."
       }
   ]

Command Line Interface
---------------------

WizardSData also provides a command-line interface:

.. code-block:: bash

   # Configure the library
   python -m wizardsdata configure --api-key "your-api-key" --client-template "templates/client.txt" --advisor-template "templates/advisor.txt" --profiles "profiles.json" --output "conversations.json" --client-model "gpt-4" --advisor-model "gpt-4"
   
   # Generate conversations
   python -m wizardsdata generate
   
   # Show current configuration
   python -m wizardsdata show-config
   
   # Save configuration to file
   python -m wizardsdata configure --config-file "config.json"
   
   # Load configuration from file
   python -m wizardsdata load-config "config.json"