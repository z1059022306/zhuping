import yaml
import os

def read_yaml_data():
    with open("./data" + os.sep, "r", encoding='utf-8') as  f:
        return yaml.load(f)