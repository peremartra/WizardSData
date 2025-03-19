Welcome to WizardSData's documentation!
=====================================

WizardSData is a Python library for generating conversation datasets using language models. It provides a simple interface for configuring, generating, and saving conversations between different roles (such as a financial advisor and a client).

.. image:: https://img.shields.io/badge/docs-latest-blue.svg
   :target: https://yourusername.github.io/wizardsdata/
   :alt: Documentation Status

Features
--------

* Configure conversation profiles and parameters
* Generate realistic conversations using language models (OpenAI)
* Save conversations in structured JSON format
* Command-line interface for easy usage
* Flexible template system for customizing conversation prompts

Quick Start
-----------

Installation
^^^^^^^^^^^

.. code-block:: bash

   pip install wizardsdata

Basic Usage
^^^^^^^^^^

.. code-block:: python

   import wizardsdata as wsd
   
   # Configure the library
   errors = wsd.set_config(
       API_KEY="your-api-key",
       template_client_prompt="templates/client.txt",
       template_advisor_prompt="templates/advisor.txt",
       file_profiles="profiles.json",
       file_output="conversations.json",
       model_client="gpt-4",
       model_advisor="gpt-4"
   )
   
   # Check if configuration is valid
   if not errors:
       # Generate conversations
       success = wsd.start_generation()
       if success:
           print("Conversations generated successfully!")

Table of Contents
----------------

.. toctree::
   :maxdepth: 2
   :caption: Contents:
   
   installation
   usage
   api
   examples
   examples_gallery

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`