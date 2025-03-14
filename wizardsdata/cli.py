"""
Command-line interface for WizardSData.
"""
import argparse
import json
import sys
from typing import Dict, Any, List

from . import set_config, get_config, is_config_valid, save_config, load_config, start_generation


def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description="WizardSData - Generate conversation datasets")
    
    subparsers = parser.add_subparsers(dest="command", help="Command to execute")
    
    # Configure command
    configure_parser = subparsers.add_parser("configure", help="Configure WizardSData")
    configure_parser.add_argument("--api-key", dest="API_KEY", help="API key for OpenAI")
    configure_parser.add_argument("--client-template", dest="template_client_prompt", 
                                  help="Path to client template file")
    configure_parser.add_argument("--advisor-template", dest="template_advisor_prompt", 
                                  help="Path to advisor template file")
    configure_parser.add_argument("--profiles", dest="file_profiles", 
                                  help="Path to profiles JSON file")
    configure_parser.add_argument("--output", dest="file_output", 
                                  help="Path to output JSON file")
    configure_parser.add_argument("--client-model", dest="model_client", 
                                  help="Model to use for client")
    configure_parser.add_argument("--advisor-model", dest="model_advisor", 
                                  help="Model to use for advisor")
    configure_parser.add_argument("--config-file", help="Save configuration to this file")
    
    # Advanced configuration
    configure_parser.add_argument("--client-temp", dest="temperature_client", type=float,
                                 help="Temperature for client model (default: 0.7)")
    configure_parser.add_argument("--client-top-p", dest="top_p_client", type=float,
                                 help="Top-p for client model (default: 0.95)")
    configure_parser.add_argument("--client-freq-pen", dest="frequency_penalty_client", type=float,
                                 help="Frequency penalty for client model (default: 0.3)")
    configure_parser.add_argument("--client-max-tokens", dest="max_tokens_client", type=int,
                                 help="Max tokens for client model (default: 175)")
    configure_parser.add_argument("--max-questions", dest="max_recommended_questions", type=int,
                                 help="Maximum number of questions (default: 10)")
    configure_parser.add_argument("--advisor-temp", dest="temperature_advisor", type=float,
                                 help="Temperature for advisor model (default: 0.5)")
    configure_parser.add_argument("--advisor-top-p", dest="top_p_advisor", type=float,
                                 help="Top-p for advisor model (default: 0.9)")
    configure_parser.add_argument("--advisor-freq-pen", dest="frequency_penalty_advisor", type=float,
                                 help="Frequency penalty for advisor model (default: 0.1)")
    configure_parser.add_argument("--advisor-max-tokens", dest="max_tokens_advisor", type=int,
                                 help="Max tokens for advisor model (default: 325)")
    
    # Load config command
    load_parser = subparsers.add_parser("load-config", help="Load configuration from file")
    load_parser.add_argument("config_file", help="Path to configuration file")
    
    # Show config command
    subparsers.add_parser("show-config", help="Show current configuration")
    
    # Generate command
    subparsers.add_parser("generate", help="Generate conversations")
    
    return parser.parse_args()


def clean_args(args_dict: Dict[str, Any]) -> Dict[str, Any]:
    """Clean argument dictionary by removing None values."""
    return {k: v for k, v in args_dict.items() if v is not None}


def main():
    """Run the command-line interface."""
    args = parse_args()
    
    if args.command == "configure":
        # Convert args to dictionary and remove None values
        config_dict = clean_args(vars(args))
        
        # Remove command and config_file
        config_dict.pop("command", None)
        config_file = config_dict.pop("config_file", None)
        
        # Set configuration
        missing = set_config(**config_dict)
        
        if missing:
            print(f"Warning: Missing mandatory parameters: {', '.join(missing)}")
        else:
            print("Configuration set successfully.")
        
        # Save configuration if requested
        if config_file:
            if save_config(config_file):
                print(f"Configuration saved to {config_file}")
            else:
                print(f"Failed to save configuration to {config_file}")
    
    elif args.command == "load-config":
        if load_config(args.config_file):
            print(f"Configuration loaded from {args.config_file}")
        else:
            print(f"Failed to load configuration from {args.config_file}")
            return 1
    
    elif args.command == "show-config":
        config = get_config()
        print(json.dumps(config, indent=2))
    
    elif args.command == "generate":
        if not is_config_valid():
            print("Configuration is not valid. Please configure WizardSData first.")
            return 1
        
        print("Starting conversation generation...")
        success = start_generation()
        
        if success:
            print("Conversations generated successfully!")
        else:
            print("Failed to generate conversations.")
            return 1
    
    else:
        print("No command specified. Use -h for help.")
        return 1
    
    return 0


if __name__ == "__main__":
    sys.exit(main())