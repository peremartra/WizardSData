.. WizardSData documentation master file, created by
   sphinx-quickstart on Sat Mar 15 19:25:23 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.
Welcome to WizardSData's documentation!
=======================================
WizardSData is a Python library for generating conversation datasets using language models. It automates the creation of simulated conversations between a client and an advisor using templates and LLM APIs.

Getting Started
--------------

Install the package:

.. code-block:: bash

   pip install wizardsdata

Basic usage:

.. code-block:: python

   import wizardsdata as wsd
   
   # Configure the library
   wsd.set_config(
       API_KEY="your-api-key",
       template_client_prompt="templates/client.j2",
       template_advisor_prompt="templates/advisor.j2",
       file_profiles="profiles.json",
       file_output="output.json",
       model_client="gpt-4o-mini",
       model_advisor="gpt-4o-mini"
   )
   
   # Start generating conversations
   wsd.start_generation()

Contents
--------

.. toctree::
   :maxdepth: 2
   
   installation
   usage
   api
   cli

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`