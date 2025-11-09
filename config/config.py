import yaml
import os

def read_config(filepath):
    try:
        with open(filepath, 'r') as file:
            data = yaml.safe_load(file)
        
        print("YAML data loaded successfully:")
        print(data)
        return data

    except FileNotFoundError:
        print("Error: 'config.yaml' not found. Please create the file.")
    except yaml.YAMLError as e:
        print(f"Error parsing YAML file: {e}")
    

if __name__ == "__main__":
    home_directory = os.path.expanduser('~')
    full_path = os.path.join(home_directory,"projects/work-helper/configs/local-dev.yaml")
    print(read_config(full_path))