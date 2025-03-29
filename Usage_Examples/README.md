# Usage Examples for WizardSData

This directory contains example use cases demonstrating how to generate synthetic datasets using the WizardSData library. These examples help users understand how different configurations, profile templates, and prompts contribute to dataset creation.

## **Current Examples**
- [**example_financial_dataset/**](https://github.com/peremartra/WizardSData/tree/main/Usage_Examples/example_financial_dataset): Demonstrates how to generate a dataset for financial conversations using a structured approach with predefined profiles and prompt templates.

## **Planned Additions**
Future examples will cover:
- Different domain-specific datasets (e.g., healthcare, customer support, legal)
- Variations in dataset generation parameters (e.g., different LLMs, prompt strategies)
- Bias analysis and dataset evaluation methods

Each example contains:
1. A **Jupyter Notebook** illustrating the dataset generation process.
2. A **configuration JSON file** specifying the parameters used.
3. The **generated dataset** in JSON format.

Refer to individual example folders for specific details on each implementation.

## Profile JSON Format

When creating your profile JSON files, include the following fields:

```json
{
  "profiles": [
    {
      "id": "unique_identifier",
      "topic": "Main Conversation Topic",
      "field1": "value1",
      "field2": "value2"
    }
  ]
}
```
