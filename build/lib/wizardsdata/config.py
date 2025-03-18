from typing import Dict, Any, List, Set, Optional
import os
import json


class Config:
    """
    Configuration manager for the WizardSData conversation generation system.
    This class handles all configuration parameters needed for generating conversations
    between clients and advisors, providing methods for setting, retrieving, and validating
    configuration values.
    Attributes:
        MANDATORY_PARAMS (set): Required configuration parameters that must be set before use.
        DEFAULT_CONFIG (dict): Default values for optional parameters.
    Configuration Parameters:
        API_KEY (str): API key for accessing external language model services.
        template_client_prompt (str): File path to the template used for client prompts.
        template_advisor_prompt (str): File path to the template used for advisor prompts.
        file_profiles (str): File path to the JSON containing conversation profiles.
        file_output (str): File path where generated conversations will be saved.
        model_client (dict): Model configuration for client responses.
        model_advisor (dict): Model configuration for advisor responses.
        Optional parameters with defaults:
        temperature_client (float): Temperature for client model sampling (default: 0.7).
        top_p_client (float): Top-p value for client model sampling (default: 0.95).
        frequency_penalty_client (float): Frequency penalty for client model (default: 0.3).
        max_tokens_client (int): Maximum tokens for client responses (default: 175).
        max_recommended_questions (int): Maximum recommended questions to generate (default: 10).
        temperature_advisor (float): Temperature for advisor model sampling (default: 0.5).
        top_p_advisor (float): Top-p value for advisor model sampling (default: 0.9).
        frequency_penalty_advisor (float): Frequency penalty for advisor model (default: 0.1).
        max_tokens_advisor (int): Maximum tokens for advisor responses (default: 325).
    Examples:
        >>> config = Config()
        >>> config.set(API_KEY="your-api-key", 
        ...           template_client_prompt="path/to/client_template.txt",
        ...           template_advisor_prompt="path/to/advisor_template.txt",
        ...           file_profiles="path/to/profiles.json",
        ...           file_output="path/to/output.json",
        ...           model_client={"name": "gpt-4"},
        ...           model_advisor={"name": "gpt-4"})
        >>> if config.is_valid():
        ...     print("Configuration is valid!")
        ... else:
        ...     print(f"Missing parameters: {config.validate()}")
        # Get specific configuration parameters
        >>> client_temp = config.get("temperature_client")
        >>> all_params = config.get_all()
    Notes:
        - The validate() method checks if all mandatory parameters are set and if
          specified file paths exist.
        - Configuration parameters can be overridden by calling set() multiple times.
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
        """
        Initialize the configuration with default values.
        This method initializes a new configuration object with the following steps:
        1. Creates an empty configuration dictionary (_config)
        2. Populates it with default values:
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
        3. Initializes an empty set to track which parameters have been explicitly set
           by the user (_set_params)
        No parameters are required as it uses class-defined defaults.
        Returns:
            None
        """

        # Start with an empty config dictionary
        self._config = {}
        
        # Add default values
        self._config.update(self.DEFAULT_CONFIG)
        
        # Keep track of what's been set
        self._set_params = set()
    
    def set(self, **kwargs) -> None:
        """
        Set a configuration parameter
       
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
        Set global configuration parameters and validate the resulting configuration.
    
        This function provides a convenient interface to set parameters in the global
        Config instance. After setting the provided parameters, it automatically
        validates the configuration and returns any validation errors.
        
        Args:
            **kwargs: Key-value pairs for configuration parameters. 
            Configuration Parameters:
            API_KEY (str): API key for accessing external language model services.
            template_client_prompt (str): File path to the template used for client prompts.
            template_advisor_prompt (str): File path to the template used for advisor prompts.
            file_profiles (str): File path to the JSON containing conversation profiles.
            file_output (str): File path where generated conversations will be saved.
            model_client (dict): Model configuration for client responses.
            model_advisor (dict): Model configuration for advisor responses.
            
            Optional parameters with defaults:
            temperature_client (float): Temperature for client model sampling (default: 0.7).
            top_p_client (float): Top-p value for client model sampling (default: 0.95).
            frequency_penalty_client (float): Frequency penalty for client model (default: 0.3).
            max_tokens_client (int): Maximum tokens for client responses (default: 175).
            max_recommended_questions (int): Maximum recommended questions to generate (default: 10).
            temperature_advisor (float): Temperature for advisor model sampling (default: 0.5).
            top_p_advisor (float): Top-p value for advisor model sampling (default: 0.9).
            frequency_penalty_advisor (float): Frequency penalty for advisor model (default: 0.1).
            max_tokens_advisor (int): Maximum tokens for advisor responses (default: 325).
        
        Returns:
            List[str]: A list of validation errors. Empty list if configuration is valid.
            
        Examples:
            >>> # Setting only partial mandatory parameters will return validation errors
            >>> errors = set_config(API_KEY="my-api-key", 
            ...                     template_client_prompt="templates/client.txt")
            >>> if errors:
            ...     print(f"Configuration is incomplete: {errors}")
            ...     # Output: Configuration is incomplete: ['template_advisor_prompt', 'file_profiles', 'file_output', 'model_client', 'model_advisor']
            >>> 
            >>> # Setting all mandatory parameters for a valid configuration
            >>> errors = set_config(
            ...     API_KEY="my-api-key",
            ...     template_client_prompt="templates/client.txt",
            ...     template_advisor_prompt="templates/advisor.txt",
            ...     file_profiles="data/profiles.json",
            ...     file_output="output/conversations.json",
            ...     model_client={"name": "gpt-4"},
            ...     model_advisor={"name": "gpt-4"}
            ... )
            >>> if not errors:
            ...     print("Configuration is valid!")
            
        Notes:
            - This updates only the parameters specified in kwargs; other parameters
            retain their current values.
            - See the Config class for a complete list of valid parameters.    
    """

    
    config.set(**kwargs)
    return config.validate()


def get_config() -> Dict[str, Any]:
    """
    Get the current global configuration.
    
    This function retrieves all current configuration parameters from the global
    Config instance, including both explicitly set values and default values.
    
    Returns:
        Dict[str, Any]: Dictionary with all configuration parameters.
        
    Examples:
        >>> full_config = get_config()
        >>> print(f"Client temperature: {full_config['temperature_client']}")
        >>> 
        >>> # Get specific parameters directly from the config instance
        >>> from wizardsdata.config import config
        >>> print(f"API Key: {config.get('API_KEY')}")
    """
    return config.get_all()


def is_config_valid() -> bool:
    """
    Check if the current global configuration is valid.
    
    This function checks if all mandatory parameters are set and if specified
    file paths exist.
    
    Returns:
        bool: True if the configuration is valid, False otherwise.
        
    Examples:
        >>> if not is_config_valid():
        ...     print("Please set all required configuration parameters")
        ...     # Show what's missing
        ...     from wizardsdata.config import config
        ...     print(f"Missing: {config.validate()}")
        
    Notes:
        - Mandatory parameters are defined in Config.MANDATORY_PARAMS
        - The function also checks if specified file paths exist
    """
    return config.is_valid()


def save_config(file_path: str) -> bool:
    """
    Save the current global configuration to a JSON file.
    
    This function exports all configuration parameters (including defaults)
    to a specified JSON file for later reuse.
    
    Args:
        file_path (str): Path where the configuration file will be saved.
        
    Returns:
        bool: True if the save operation was successful, False otherwise.
        
    Examples:
        >>> success = save_config("config/my_project_config.json")
        >>> if success:
        ...     print("Configuration saved successfully!")
        ... else:
        ...     print("Failed to save configuration")
        
    Notes:
        - The saved file uses JSON format with 4-space indentation
        - Both explicitly set and default values are saved
    """
    try:
        with open(file_path, 'w') as f:
            json.dump(config.get_all(), f, indent=4)
        return True
    except Exception:
        return False


def load_config(file_path: str) -> bool:
    """
    Load configuration from a JSON file into the global config instance.
    
    This function reads a previously saved configuration file and updates
    the global Config instance with those values.
    
    Args:
        file_path (str): Path to the configuration JSON file.
        
    Returns:
        bool: True if the load operation was successful, False otherwise.
        
    Examples:
        >>> success = load_config("config/my_project_config.json")
        >>> if success:
        ...     print("Configuration loaded successfully!")
        ...     # Check if it's complete
        ...     if is_config_valid():
        ...         print("And it's valid!")
        ... else:
        ...     print("Failed to load configuration")
        
    Notes:
        - This overwrites any previously set parameters with values from the file
        - Parameters not specified in the file retain their current values
        - The function silently catches and handles any exceptions during loading.
    """
    try:
        with open(file_path, 'r') as f:
            config_data = json.load(f)
        config.set(**config_data)
        return True
    except Exception:
        return False