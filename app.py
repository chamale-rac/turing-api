from src.utils.tools import readYaml
from src.turing import Turing

path = './assets/LAB9E2.yaml'
path = './assets/LAB9E3.yaml'
path = './assets/LAB10E1.yaml'

crudeConfig = readYaml(path)
turing = Turing(crudeConfig)

turing.goSimulation()
