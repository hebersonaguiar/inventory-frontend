import json, re, csv, requests, datetime
from flask import Flask, render_template, request, redirect, url_for, flash, stream_with_context, g, session
from flask_restful import Resource, Api
# from flask_mysqldb import MySQL
from flask_cors import CORS
from flask_jsonpify import jsonify
from json import dumps
# from datetime import datetime

app = Flask(__name__)
api = Api(app)
CORS(app, resources={r"/*": {"origins": "*"}})
app.secret_key = "flash message"


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/servers', methods=['GET'])
def servers():
    try:

        api_url = "http://inventory:5000/hosts"
        response = requests.get(api_url)

        if response.status_code == 200:
             data = json.loads(response.text)
            #  print(data) #pint json list
        else:
             print(f"Error retrieving data, status code: {response.status_code}")

        return render_template('servers.html', hosts=data)
        # return response.json()

    except Exception as e:
        # return redirect(url_for('servers'))
        print(e)
        return redirect(url_for('index'))
    
@app.route('/edit/<string:servername>', methods=['GET'])
def edit(servername):
    try:

        api_url = "http://inventory:5000/hosts/{}".format(servername)
        response = requests.get(api_url)

        if response.status_code == 200:
             data = json.loads(response.text)
            #  print(data) #pint json list
        else:
             print(f"Error retrieving data, status code: {response.status_code}")

        return render_template('edit.html', edit=data)
        # return response.json()

    except Exception as e:
        # return redirect(url_for('servers'))
        print(e)
        return redirect(url_for('index'))
    

@app.route('/updateinventory', methods=['POST'])
def updateinventory():
    try:
        now = datetime.datetime.now()
        hostname = request.form.get('hostname')
        url = request.form.get('url')
        environnment = request.form.get('environnment')
        cluster = request.form.get('cluster')
        publicacao = request.form.get('publicacao')
        middleware = request.form.get('middleware')
        framework = request.form.get('framework')
        linguagem = request.form.get('linguagem')
        prioridade = request.form.get('prioridade')
        risco = request.form.get('risco')
        sigla = request.form.get('sigla')
        datacenter = request.form.get('datacenter')
        repositorio = request.form.get('repositorio')
        nacionalcjf = request.form.get('nacionalcjf')
        objetivo = request.form.get('objetivo')
        updated_at = now.strftime("%Y-%m-%d %H:%M")

        print(hostname)
        print(url)
        print(environnment)
        print(cluster)
        print(publicacao)
        print(middleware)
        print(framework)
        print(linguagem)
        print(prioridade)
        print(risco)
        print(sigla)
        print(datacenter)
        print(repositorio)
        print(nacionalcjf)
        print(objetivo)
        print(updated_at)

        return redirect(url_for('servers'))

    except Exception as e:
        print(e)
        return redirect(url_for('servers'))


if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port='5000')