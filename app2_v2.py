import os
from flask import Flask, render_template, json, request, jsonify

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html')

@app.route('/teste', methods=['GET'])
def teste():
    return render_template('testejson.html')


@app.route('/teste', methods=['POST'])
def teste1():
    json = request.get_json()
    nomeCompleto = json['nomeCompleto']
    idEmail = json['idEmail']
    return jsonify(nomeCompleto=nomeCompleto, idEmail=idEmail)


@app.route('/testejson', methods=['GET'])
def teste2():
    return render_template('testejson2.html')


@app.route('/testejson', methods=['POST'])
def teste3():
    nomeCompleto = request.form['nomeCompleto']
    idEmail = request.form['idEmail']
    print(nomeCompleto)
    print(idEmail)
    return jsonify(nomeCompleto=nomeCompleto)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='localhost', port=port)