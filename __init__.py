"""
WizardSData - A library for generating conversation datasets using language models.
"""

__version__ = '0.1.0'

from .config import set_config, get_config, is_config_valid, save_config, load_config
from .generator import start_generation

# Export public API
__all__ = [
    'set_config',
    'get_config',
    'is_config_valid',
    'save_config',
    'load_config',
    'start_generation',
]