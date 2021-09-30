import yaml
import os



def read_yml(path_to_yml: str) -> dict:
    with open(path_to_yml) as yaml_file:
        content = yaml.safe_load(yaml_file)

    return content
