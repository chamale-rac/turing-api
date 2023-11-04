import yaml
import tabulate


def readYaml(path: str) -> any:
    '''
    Read a yaml file and return its content
    '''
    with open(path, 'r') as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError:
            return None


def readBase64Yaml(base64: str) -> any:
    '''
    Read a base64 yaml file and return its content
    '''
    try:
        return yaml.safe_load(base64)
    except yaml.YAMLError:
        return None


def strTable(columns, data):
    '''
    String a table
    '''
    return tabulate.tabulate(data, columns, tablefmt='pipe')
