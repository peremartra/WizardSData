"""
Utility functions for WizardSData.
"""
import os
import json
from typing import Dict, Any, List, Optional


def ensure_directory_exists(file_path: str) -> bool:
    """
    Ensure the directory for a file exists, creating it if necessary.
    
    Args:
        file_path: Path to the file.
        
    Returns:
        True if directory exists or was created, False otherwise.
    """
    try:
        directory = os.path.dirname(file_path)
        if directory and not os.path.exists(directory):
            os.makedirs(directory, exist_ok=True)
        return True
    except Exception:
        return False


def load_json(file_path: str) -> Optional[Dict[str, Any]]:
    """
    Load JSON data from a file.
    
    Args:
        file_path: Path to the JSON file.
        
    Returns:
        Dictionary with JSON data, or None if failed.
    """
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except Exception as e:
        print(f"Error loading JSON from {file_path}: {str(e)}")
        return None


def save_json(data: Any, file_path: str) -> bool:
    """
    Save data to a JSON file.
    
    Args:
        data: Data to save.
        file_path: Path to save the JSON file.
        
    Returns:
        True if successful, False otherwise.
    """
    try:
        ensure_directory_exists(file_path)
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
        return True
    except Exception as e:
        print(f"Error saving JSON to {file_path}: {str(e)}")
        return False