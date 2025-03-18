"""
WizardSData - A library for generating conversation datasets using language models.
"""

__version__ = '0.1.0'

try:
    from .config import set_config, get_config, is_config_valid, save_config, load_config
    from .generator import start_generation
except ImportError as e:
    print(f"Error importing wizardsdata modules: {e}")
    print("Please ensure all modules are correctly named and present.")
    raise

# Export public API
__all__ = [
    'set_config',
    'get_config',
    'is_config_valid',
    'save_config',
    'load_config',
    'start_generation',
]

def main():
    """Entry point for the command-line interface."""
    from .cli import main as cli_main
    return cli_main()