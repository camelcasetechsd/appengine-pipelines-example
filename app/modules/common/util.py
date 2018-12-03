import os
import yaml

def ReadYamlFile(fileLocation):
        data = {}
        yaml_path = os.path.join(os.path.dirname(__file__), fileLocation)
        with open(yaml_path, 'r') as stream:
                data = yaml.load(stream)

        return data