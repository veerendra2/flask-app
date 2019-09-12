'''
Author: Veerendra Kakumanu
Description: Coverts HEX color representation to RGB
'''
from flask import Flask
from flask import request
from prometheus_flask_exporter import PrometheusMetrics
import json
import re

PATTREN = r'^#[0-9A-F]{6}$'

app = Flask(__name__)
metrics = PrometheusMetrics(app)
metrics.info('app_info', ' Coverts HEX color representation to RGB', version='0.1')

@app.route('/', methods=['POST'])
@metrics.gauge('in_progress', 'Long running requests in progress')
def convert():
    data = request.get_json(force=True)
    if "code" not in data or re.match(PATTREN, data["code"].upper()) is None:
        return json.dumps({"result": "Invalid POST data/HEX color code"}), 400
    code = data["code"].lstrip('#')
    rgb_tuple = tuple(int(code[i:i+2], 16) for i in (0, 2, 4))
    return json.dumps({"result": "RGB"+str(rgb_tuple)}), 200

@app.route('/', methods=['GET', 'PUT', 'DELETE'])
def handle_non_get():
    return "", 200

if __name__ == '__main__':
    app.run()

