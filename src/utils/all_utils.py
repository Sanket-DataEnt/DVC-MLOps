import yaml
import os



def read_yaml(path_to_yml: str) -> dict:
    with open(path_to_yml) as yaml_file:
        content = yaml.safe_load(yaml_file)

    return content

def create_directory(dirs: list):
    for dir_path in dirs:
        os.makedirs(dir_path, exist_ok=True)
        print(f"directory is created at {dir_path}")
