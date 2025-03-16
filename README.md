
# WizardSData

![Generate Syntetic Conversations](/images/wizardsdata_banner.png)

<div align="center">
    <h3>
        <a href="https://peremartra.github.io/WizardSData/build/html/index.html" target="_blank">DOCUMENTATION</a> | 
        <a href="https://github.com/peremartra/WizardSData/tree/main/Usage_Examples" target="_blank">EXAMPLES</a>
    </h3>
</div>


A Python library for generating conversation datasets using language models. WizardSData automates the creation of simulated conversations between a client and an advisor, using templates and model APIs.

This library is perfect for generating dialogues in highly regulated sectors like Finance or Healthcare, where the use of customer data is strictly protected.

The generated dialogues can be used to train or fine-tune large language models.

## ¿How it works? 
The library simulates a conversation between two people. One initiates the dialogue and is represented by one of the profiles from the `profiles` file. The other acts as the respondent, generated using information contained, also, in the profile. Therefore, if desired, the profile can include information about two different people, turning it into a conversation profile instead of a role profile.

For the library to start generating conversations, it requires a profiles file and two prompt templates. Each profile in the `profiles` file will define the personality or personalities part of the conversation. Different examples can be found in the `templates` directory.

A basic usage example can be found in `usage_examples/basic_usage.py`.

### Let's analyze one of the examples: financial01. 
In this example, we find different profile files that only vary in the number of profiles they contain. They represent various profiles from Retail Banking, requesting information about products such as home deposit accounts, pension plans, or medium and long-term investments.
#### Profile Creation 
In the `profiles` directory, you will find different files containing varying numbers of profiles. Let's take a look at  `financial_sample01_2.json`

```json
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
```
This JSON file defines two different profiles:
* A 30-year-old single Spanish IT professional looking for information on how to save for buying a house.
* A 45-year-old marketing manager interested in setting up a pension plan.

The fields to use are completely flexible, meaning the profiles can include any information you consider necessary. This information will be used to create the prompts sent to the language model to simulate the behavior of each of the two roles.

#### Prompt templates. 
A template must be defined for each prompt. Let's look at the two templates used in this example, both of which can be found in the prompts directory.

**Client Prompt Template**
```j2
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
```

**Advisor Prompt Template.** 
```j2
You are an expert financial advisor specializing in {{ profile.financial_goal | lower }}.

Client Context:
- The client is approximately {{ profile.age }} years old, {{ profile.marital_status | lower }}, and appears to be a {{ profile.profession | lower }} from {{ profile.country }}.
- The client's financial goal is to {{ profile.financial_goal | lower }}.

Instructions for the conversation:
- Start by greeting the client and asking relevant, natural questions to understand their financial situation, preferences, and concerns.
- Guide the conversation by asking about their current financial products, investment experience, and risk tolerance.
- Provide clear, concise, and professional advice tailored to the client's goal and profile as the information is revealed.
- Avoid using complex financial jargon unless necessary, and adapt your language to the client's knowledge level (you'll assess this through conversation).
- Focus on actionable recommendations to help the client achieve their goal.
- Keep the conversation realistic and friendly.
- End the conversation naturally once you believe the client's doubts have been resolved, or explicitly conclude by saying '[END]'
```
As you can see, the information in both templates is filled using the data from the profile fields.
## Installation

Install directly from GitHub:

```bash
pip install git+https://github.com/peremartra/WizardSData.git
```



## Features

- Generate simulated conversations between clients and advisors
- Use templates to create dynamic prompts based on user profiles
- Configure model parameters for both client and advisor sides
- Save conversations in structured JSON format

## Quick Start

```python
import wizardsdata as wsd

# Configure the library
wsd.set_config(
    API_KEY="your-api-key",
    template_client_prompt="path/to/client_template.j2",
    template_advisor_prompt="path/to/advisor_template.j2",
    file_profiles="path/to/profiles.json",
    file_output="path/to/output.json",
    model_client="gpt-4o-mini",
    model_advisor="gpt-4o-mini"
)

# Start generating conversations
success = wsd.start_generation()
if success:
    print("Conversations generated successfully!")
else:
    print("Failed to generate conversations.")
```

## Template Format

The library uses Jinja2 templates for generating client and advisor prompts. Here's an example of a client template:

```jinja
You are a financial client with the following profile:
- Age: {{ profile.age }}
- Marital status: {{ profile.marital_status }}
- Country: {{ profile.country }}
- Financial goal: {{ profile.financial_goal }}

You want to ask an advisor about {{ profile.financial_goal }}.

Please conduct a conversation with the advisor, asking relevant questions.
If you feel satisfied with the advice, end the conversation with "[END]".
You can ask up to {{ max_questions }} questions.
```

## Profile Format

Profiles should be provided in JSON format:

```json
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
    ...
  ]
}
```

All fields, but `id` are optional and you can create your own fields. 

## Configuration Parameters

### Mandatory Parameters

- `API_KEY`: Your OpenAI API key
- `template_client_prompt`: Path to the client template file
- `template_advisor_prompt`: Path to the advisor template file
- `file_profiles`: Path to the profiles JSON file
- `file_output`: Path to save the output JSON file
- `model_client`: Model to use for the client
- `model_advisor`: Model to use for the advisor

### Optional Parameters (with defaults)

#### Client Configuration
- `temperature_client`: 0.7
- `top_p_client`: 0.95
- `frequency_penalty_client`: 0.3
- `max_tokens_client`: 175
- `max_recommended_questions`: 10

#### Advisor Configuration
- `temperature_advisor`: 0.5
- `top_p_advisor`: 0.9
- `frequency_penalty_advisor`: 0.1
- `max_tokens_advisor`: 325

## Advanced Usage

### Saving and Loading Configuration

```python
import wizardsdata as wsd

# Set initial configuration
wsd.set_config(API_KEY="your-api-key", ...)

# Save configuration for later use
wsd.save_config("config.json")

# Later, load the saved configuration
wsd.load_config("config.json")

# Start generation with loaded config
wsd.start_generation()
```

## License

Apache-2.0 license
