#import pandas as pd
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def homepage():
  return 'Essa é a homepage do site (API) de Leo. (API) está no ar'

@app.route('/DicionarioParaJson')
def DicionarioParaJson():
  Dicionario = {'teste': 123456789}
  print(Dicionario)
  return jsonify(Dicionario)

app.run(host='0.0.0.0')