import yaml
import tabulate
import base64


def readYaml(path: str) -> any:
    '''
    Read a yaml file and return its content
    '''
    with open(path, 'r') as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError:
            return None


def readBase64Yaml(base64_string: str) -> any:
    '''
    Read a base64 yaml file and return its content
    '''
    # Decode the base64 string
    decoded_string = base64.b64decode(base64_string).decode()

    try:
        return yaml.safe_load(decoded_string)
    except yaml.YAMLError:
        return None


def strTable(columns, data):
    '''
    String a table
    '''
    return tabulate.tabulate(data, columns, tablefmt='pipe')
