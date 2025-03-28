Installation
============

Requirements
-----------

WizardSData requires:

* Python 3.8 or higher
* OpenAI API key
* Dependencies:
  - openai
  - jinja2

Installing from PyPI
-------------------

The recommended way to install WizardSData is from PyPI:

.. code-block:: bash

   pip install wizardsdata

Installing from Source
---------------------

Alternatively, you can install from the source code:

.. code-block:: bash

   git clone https://github.com/yourusername/wizardsdata.git
   cd wizardsdata
   pip install -e .

Verifying Installation
---------------------

You can verify the installation by importing the package in Python:

.. code-block:: python

   import wizardsdata
   
   # Print the version
   print(wizardsdata.__version__)

API Key Setup
------------

Before using WizardSData, you need to obtain an OpenAI API key. You can get one by signing up at the `OpenAI website <https://platform.openai.com/signup>`_.

Once you have your API key, you can provide it when configuring the library:

.. code-block:: python

   import wizardsdata as wsd
   
   wsd.set_config(API_KEY="your-api-key", ...)

Or use it from an environment variable:

.. code-block:: python

   import os
   import wizardsdata as wsd
   
   api_key = os.environ.get("OPENAI_API_KEY")
   wsd.set_config(API_KEY=api_key, ...)