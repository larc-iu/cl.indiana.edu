import yaml
import os
from pelican import signals

def load_yaml_data(generator):
    """Load YAML data files and make them available to templates"""
    try:
        yaml_files = {}
        content_path = generator.settings.get('PATH', 'content')
        # Look for YAML files in content directory
        for root, dirs, files in os.walk(content_path):
            for file in files:
                if file.endswith('.yaml') or file.endswith('.yml'):
                    file_path = os.path.join(root, file)
                    with open(file_path, 'r', encoding='utf-8') as f:
                        yaml_data = yaml.safe_load(f)
                        # Make available as filename without extension
                        key = os.path.splitext(file)[0]
                        yaml_files[key] = yaml_data
        
        # Add to Jinja2 environment
        generator.env.globals['yaml_data'] = yaml_files
    except Exception as e:
        print(f"Error in yaml_loader: {e}")

def register():
    signals.generator_init.connect(load_yaml_data)