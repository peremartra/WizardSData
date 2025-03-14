"""
Template handling for WizardSData.
"""
import os
from typing import Dict, Any, Optional
from jinja2 import Template


def render_prompt_from_path(template_path: str, profile: Dict[str, Any], **kwargs) -> str:
    """
    Render a prompt template from a specific file path with the given profile and additional variables.
    
    Args:
        template_path: Path to the template file.
        profile: Dictionary with profile data.
        **kwargs: Additional variables to use in the template.
        
    Returns:
        The rendered template as a string, or empty string if failed.
    """
    try:
        # Check if the template file exists
        if not os.path.exists(template_path):
            print(f"Error: Template file not found: {template_path}")
            return ""
        
        # Read template content
        with open(template_path, 'r', encoding='utf-8') as f:
            template_content = f.read()
            
        # Check if the template is empty
        if not template_content.strip():
            print(f"Warning: Template file is empty: {template_path}")
            return ""
            
        # Create a Template directly from the string
        template = Template(template_content)
        
        # Render the template
        result = template.render(profile=profile, **kwargs)
        
        return result
    except Exception as e:
        print(f"Error rendering template: {str(e)}")
        return ""