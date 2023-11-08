from flask import Flask, jsonify, request
from flask_cors import CORS
from src.utils.tools import readBase64Yaml
from src.turing import Turing

app = Flask(__name__)
CORS(app)


@app.route('/turing', methods=['POST'])
def work_simulation():
    data = request.json
    yamlFileStringBase64 = data['file']  # type: ignore
    crudeConfig = readBase64Yaml(yamlFileStringBase64)
    turing = Turing(crudeConfig)
    results = turing.goSimulation()

    response = []

    keys = ['accept', 'head', 'body',
            'stringSimulation', 'message', 'solution']
    response = [dict(zip(keys, result)) for result in results]  # type: ignore

    response = {
        'response': response,
    }
    return jsonify(response), 200


@app.route("/healthz", methods=['GET'])
def salute():
    return 'Hello from iTuring server!', 200
