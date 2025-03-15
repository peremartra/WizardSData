# Configuration file for the Sphinx documentation builder

# -- Path setup --------------------------------------------------------------
import os
import sys
sys.path.insert(0, os.path.abspath('../..'))

# -- Project information -----------------------------------------------------
project = 'WizardSData'
copyright = '2025, Your Name'
author = 'Your Name'
release = '0.1.0'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',          # Core extension for API documentation
    'sphinx.ext.viewcode',         # Adds links to view source code
    'sphinx.ext.napoleon',         # Supports Google and NumPy style docstrings
    'sphinx_autodoc_typehints',    # Adds support for PEP 484 type hints
]

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# -- Extension configuration -------------------------------------------------

# Configure autodoc to only document what's in __all__
autodoc_default_options = {
    'members': None,               # Document members and __init__
    'undoc-members': False,        # Don't include undocumented members
    'private-members': False,      # Don't include private members (starting with _)
    'special-members': False,      # Don't include special members (like __special__)
    'imported-members': False,     # Don't include imported members
    'show-inheritance': True,      # Show base classes
}

# Focus on the package's public API
autodoc_member_order = 'bysource'  # Order members as they appear in the source

# Set the default role for `` to be :obj: so we can reference Python objects easily
default_role = 'obj'

# Add the roles for Python objects
python_use_unqualified_type_names = True

# Support Google-style docstrings
napoleon_google_docstring = True
napoleon_numpy_docstring = False
napoleon_include_init_with_doc = True
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = False

# Improve type hints rendering
autodoc_typehints = 'description'  # Show type hints in the description, not signature
autodoc_typehints_format = 'short' # Use short names for types

# If you're using the Read the Docs theme, you can use this for better GitHub Pages compatibility
html_theme_options = {
    'canonical_url': '',
    'logo_only': False,
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,
    'style_nav_header_background': '#2980B9',
    # Toc options
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False
}

# Make sure static paths are correctly included
html_static_path = ['_static']

# Use a stable path for _static files
html_context = {
    'css_files': [
        '_static/css/theme.css',
    ],
}

# Explicitly set URLs to be relative
html_use_index = True
html_use_modindex = True
html_use_smartypants = True
html_baseurl = '.'  # Important for GitHub Pages