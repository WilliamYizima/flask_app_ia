import os

from flask import Flask, jsonify, request
from dotenv import load_dotenv

from helper.helper import cria_randomico

load_dotenv()

APP_SETTINGS = os.getenv("APP_SETTINGS")

app = Flask(__name__)

app.config.from_object(APP_SETTINGS)
testeDanilo = os.getenv("TESTE")

@app.route('/')
def test():
    print(testeDanilo)
    return jsonify({'message':'ola'}), 200

@app.route('/insert', methods=["POST"])
def get_post():
    payload = request.get_json(force=True)
    minha_var = payload['test']
    numero_randomico = cria_randomico()
    return jsonify({'test':f' você escreveu {minha_var}','number':numero_randomico}), 200

if __name__ == '__main__':
    app.run()