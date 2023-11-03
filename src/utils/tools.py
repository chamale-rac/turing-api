import yaml


def readYaml(path: str) -> any:
    '''
    Read a yaml file and return its content
    '''
    with open(path, 'r') as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError:
            return None
