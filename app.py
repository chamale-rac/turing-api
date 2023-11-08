from src.utils.tools import readYaml, strTable
from src.turing import Turing

path = './assets/LAB9E2.yaml'
path = './assets/LAB9E3.yaml'
path = './assets/LAB10E1.yaml'
path = './assets/FLIP.yaml'

path = input('Enter path to YAML file (examples on ./assets directory): ')

crudeConfig = readYaml(path)
turing = Turing(crudeConfig)

results = turing.goSimulation()

for accept, head, body, string, message, solution in results:
    print(f'Input string: {string}')
    print(f'Accepted: {accept}')
    print(f'Head: {head}')
    print(strTable(['Transition', 'Tape'], body))
    print(f'Solution: {solution}')
    print(f'Message: {message}')
    print('='*100)
