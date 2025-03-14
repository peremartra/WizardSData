# WizardSData

A Python library for generating conversation datasets using language models. WizardSData automates the creation of simulated conversations between a client and an advisor, using templates and model APIs.

## Installation

```bash
pip install wizardsdata
```

Or install directly from GitHub:

```bash
pip install git+https://github.com/yourusername/WizardSData.git
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