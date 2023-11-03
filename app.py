from src.utils.tools import readYaml
from src.turing import Turing

path = './assets/LAB9E2.yaml'
crudeConfig = readYaml(path)
turing = Turing(crudeConfig)

turing.goSimulation()
