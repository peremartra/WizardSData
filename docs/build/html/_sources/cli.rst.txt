Command Line Interface
=====================

WizardSData provides a command-line interface for easy use.

Configuration
------------

Set up the configuration:

.. code-block:: bash

    # Set configuration
    wizardsdata configure --api-key "your-api-key" \
                         --client-template "templates/client.j2" \
                         --advisor-template "templates/advisor.j2" \
                         --profiles "profiles.json" \
                         --output "output.json" \
                         --client-model "gpt-4o-mini" \
                         --advisor-model "gpt-4o-mini"

Load a saved configuration:

.. code-block:: bash

    wizardsdata load-config config.json

Show current configuration:

.. code-block:: bash

    wizardsdata show-config

Generation
---------

Generate conversations using the current configuration:

.. code-block:: bash

    wizardsdata generate

Advanced Options
--------------

Set advanced options:

.. code-block:: bash

    wizardsdata configure --client-temp 0.8 \
                         --client-top-p 0.9 \
                         --max-questions 8 \
                         --advisor-temp 0.6 \
                         --advisor-max-tokens 400

All Available Options
-------------------

.. code-block:: text

    --api-key API_KEY           API key for OpenAI
    --client-template TEMPLATE  Path to client template file
    --advisor-template TEMPLATE Path to advisor template file
    --profiles PROFILES         Path to profiles JSON file
    --output OUTPUT             Path to output JSON file
    --client-model MODEL        Model to use for client
    --advisor-model MODEL       Model to use for advisor
    --config-file FILE          Save configuration to this file
    --client-temp TEMP          Temperature for client model (default: 0.7)
    --client-top-p TOP_P        Top-p for client model (default: 0.95)
    --client-freq-pen FREQ_PEN  Frequency penalty for client model (default: 0.3)
    --client-max-tokens TOKENS  Max tokens for client model (default: 175)
    --max-questions NUM         Maximum number of questions (default: 10)
    --advisor-temp TEMP         Temperature for advisor model (default: 0.5)
    --advisor-top-p TOP_P       Top-p for advisor model (default: 0.9)
    --advisor-freq-pen FREQ_PEN Frequency penalty for advisor model (default: 0.1)
    --advisor-max-tokens TOKENS Max tokens for advisor model (default: 325)