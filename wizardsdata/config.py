"""
Configuration management for WizardSData.
"""
from typing import Dict, Any, List, Set, Optional
import os
import json


class Config:
    """
    Configuration class for WizardSData.
    
    This class manages the configuration for the conversation generation process,
    including API keys, template paths, and model parameters.
    """
    
    # Define mandatory parameters
    MANDATORY_PARAMS = {
        'API_KEY',
        'template_client_prompt',
        'template_advisor_prompt',
        'file_profiles',
        'file_output',
        'model_client',
        'model_advisor'
    }
    
    # Define default values for optional parameters
    DEFAULT_CONFIG = {
        # Client configuration
        'temperature_client': 0.7,
        'top_p_client': 0.95,
        'frequency_penalty_client': 0.3,
        'max_tokens_client': 175,
        'max_recommended_questions': 10,
        
        # Advisor configuration
        'temperature_advisor': 0.5,
        'top_p_advisor': 0.9,
        'frequency_penalty_advisor': 0.1,
        'max_tokens_advisor': 325,
    }
    
    def __init__(self):
        """Initialize with default values."""
        # Start with an empty config dictionary
        self._config = {}
        
        # Add default values
        self._config.update(self.DEFAULT_CONFIG)
        
        # Keep track of what's been set
        self._set_params = set()
    
    def set(self, **kwargs) -> None:
        """
        Set configuration parameters.
        
        Args:
            **kwargs: Key-value pairs for configuration parameters.
        """
        # Update the configuration
        self._config.update(kwargs)
        
        # Track what's been set
        self._set_params.update(kwargs.keys())
    
    def get(self, param: str, default: Any = None) -> Any:
        """
        Get a configuration parameter.
        
        Args:
            param: Parameter name.
            default: Default value if parameter doesn't exist.
            
        Returns:
            The parameter value or the default value.
        """
        return self._config.get(param, default)
    
    def get_all(self) -> Dict[str, Any]:
        """
        Get all configuration parameters.
        
        Returns:
            Dictionary with all parameters.
        """
        return self._config.copy()
    
    def validate(self) -> List[str]:
        """
        Validate the configuration.
        
        Returns:
            List of missing mandatory parameters.
        """
        # Check for missing mandatory parameters
        missing = [param for param in self.MANDATORY_PARAMS if param not in self._config or self._config[param] is None]
        
        # Check if file paths exist
        for param in ['template_client_prompt', 'template_advisor_prompt', 'file_profiles']:
            if param in self._config and self._config[param] is not None:
                if not os.path.exists(self._config[param]):
                    missing.append(f"{param} (file not found: {self._config[param]})")
        
        return missing
    
    def is_valid(self) -> bool:
        """
        Check if configuration is valid.
        
        Returns:
            True if valid, False otherwise.
        """
        return len(self.validate()) == 0


# Create a global config instance
config = Config()


def set_config(**kwargs) -> List[str]:
    """
    Set the configuration for WizardSData.
    
    Args:
        **kwargs: Configuration parameters.
        
    Returns:
        List of missing mandatory parameters, or empty list if all is valid.
    """
    config.set(**kwargs)
    return config.validate()


def get_config() -> Dict[str, Any]:
    """
    Get the current configuration.
    
    Returns:
        Dictionary with all configuration parameters.
    """
    return config.get_all()


def is_config_valid() -> bool:
    """
    Check if the current configuration is valid.
    
    Returns:
        True if valid, False otherwise.
    """
    return config.is_valid()


def save_config(file_path: str) -> bool:
    """
    Save the current configuration to a file.
    
    Args:
        file_path: Path to save the configuration file.
        
    Returns:
        True if successful, False otherwise.
    """
    try:
        with open(file_path, 'w') as f:
            json.dump(config.get_all(), f, indent=4)
        return True
    except Exception:
        return False


def load_config(file_path: str) -> bool:
    """
    Load configuration from a file.
    
    Args:
        file_path: Path to the configuration file.
        
    Returns:
        True if successful, False otherwise.
    """
    try:
        with open(file_path, 'r') as f:
            config_data = json.load(f)
        config.set(**config_data)
        return True
    except Exception:
        return False