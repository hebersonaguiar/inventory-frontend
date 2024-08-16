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
    return render_template('govbr.html')
    # return render_template('index.html')

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

        # return render_template('servers.html', hosts=data)
        return render_template('govbrservers.html', hosts=data)
        # return response.json()

    except Exception as e:
        # return redirect(url_for('servers'))
        print(e)
        return redirect(url_for('govbr.html'))
        # return redirect(url_for('index'))
    
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

        return render_template('govbredit.html', edit=data)
        # return render_template('edit.html', edit=data)
        # return response.json()

    except Exception as e:
        # return redirect(url_for('servers'))
        print(e)
        return redirect(url_for('govbr.html'))
        return redirect(url_for('index'))
    

@app.route('/updateinventory', methods=['POST'])
def updateinventory():
    try:
        # hostname = request.form.get('hostname-up')
        # url = request.form.get('url')
        # environnment = request.form.get('environnment')
        # cluster = request.form.get('cluster')
        # publicacao = request.form.get('publication')
        # middleware = request.form.get('midleware')
        # framework = request.form.get('framework')
        # linguagem = request.form.get('app_language')
        # prioridade = request.form.get('priority')
        # risco = request.form.get('risk')
        # sigla = request.form.get('acronym')
        # datacenter = request.form.get('datacenter')
        # repositorio = request.form.get('repository')
        # nacionalcjf = request.form.get('nacionalcjf')
        # objetivo = request.form.get('goal')       

        hostname = request.form.get('hostname-up')
        print("Hostname: ", hostname)
        cluster = request.form.get('cluster')
        print("Cluster: ", cluster)
        url = request.form.get('url')
        print("URL: ", url)
        scope = request.form.get('scope')
        print("Scope: ", scope)
        middleware = request.form.get('middleware')
        print("Middleware: ", middleware)
        framework = request.form.get('framework')
        print("Framework: ", framework)
        app_language = request.form.get('app_language')
        print("App Language: ", app_language)
        db_server = request.form.get('db_server')
        print("Database Server: ", db_server)
        db_name = request.form.get('db_name')
        print("Database Name: ", db_name)
        db_schema = request.form.get('db_schema')
        print("Database Schema: ", db_schema)
        db_user = request.form.get('db_user')
        print("Database User: ", db_user)
        db_type = request.form.get('db_type')
        print("Database Type: ", db_type)
        kubernetes = request.form.get('kubernetes')
        print("Kubernetes: ", kubernetes)
        arch_ref = request.form.get('arch_ref')
        print("Arch Ref: ", arch_ref)
        monitoring_z = request.form.get('monitoring_z')
        print("Monitoramento Zabbix: ", monitoring_z)
        situation = request.form.get('situation')
        print("Situation: ", situation)
        backup = request.form.get('backup')
        print("Backup: ", backup)
        repository = request.form.get('repository')
        print("Repository: ", repository)
        type = request.form.get('type')
        print("Type: ", type)
        auth = request.form.get('auth')
        print("Auth: ", auth)
        permission = request.form.get('permission')
        print("Permission: ", permission)
        responsible_cad = request.form.get('responsible_cad')
        print("Responsible Cad: ", responsible_cad)
        responsible_permission = request.form.get('responsible_permission')
        print("Responsible Permission: ", responsible_permission)
        manager = request.form.get('manager')
        print("Manager: ", manager)
        manager_substitute = request.form.get('manager_substitute')
        print("Manager Subistituto: ", manager_substitute)
        unit = request.form.get('unit')
        print("Unit: ", unit)
        concierge_manager = request.form.get('concierge_manager')
        print("Concierge Manager: ", concierge_manager)
        sei_processor = request.form.get('sei_processor')
        print("SEI Processor: ", sei_processor)
        observation = request.form.get('observation')
        print("Observation: ", observation)
        priority = request.form.get('priority')
        print("Priority: ", priority)
        acronym = request.form.get('acronym')
        print("Acronym: ", acronym)
        sti_action = request.form.get('sti_action')
        print("STI Action: ", sti_action)
        name = request.form.get('name')
        print("Name: ", name)
        datacenter = request.form.get('datacenter')
        print("Datacenter: ", datacenter)
        goal = request.form.get('goal')
        print("Goal: ", goal)
        national_cjf = request.form.get('nacionalcjf')
        print("National/CJF: ", national_cjf)
        now = datetime.datetime.now()
        updated_at = now.strftime("%Y-%m-%d %H:%M")


        if re.search(r"-h$", hostname):
             environment = "Homologação"
        elif re.search(r"-d$", hostname):
             environment = "Desenvolvimento"
        else:
            environment = "Produção"

        print("Environment: ", environment)

        if None not in(hostname):
             update_inventory = requests.put('http://inventory:5000/v1/updateiventory/{}'.format(hostname), data=json.dumps({
                  'cluster': cluster,
                  'url': url,
                  'scope': scope,
                  'middleware': middleware,
                  'framework': framework,
                  'app_language': app_language,
                  'environment': environment,
                  'db_server': db_server,
                  'db_name': db_name,
                  'db_schema': db_schema,
                  'db_user': db_user,
                  'db_type': db_type,
                  'kubernetes': kubernetes,
                  'arch_ref': arch_ref,
                  'monitoring_z': monitoring_z,
                  'situation': situation,
                  'backup': backup,
                  'repository': repository,
                  'type': type,
                  'auth': auth,
                  'permission': permission,
                  'responsible_cad': responsible_cad,
                  'responsible_permission': responsible_permission,
                  'manager': manager,
                  'manager_substitute': manager_substitute,
                  'unit': unit,
                  'concierge_manager': concierge_manager,
                  'sei_processor': sei_processor,
                  'observation': observation,
                  'priority': priority,
                  'acronym': acronym,
                  'sti_action': sti_action,
                  'name': name,
                  'datacenter': datacenter,
                  'goal': goal,
                  'national_cjf': national_cjf,
                  'updated_at': updated_at}), 
                headers={'Content-Type':'application/json'})
             

        return redirect(url_for('servers'))

    except Exception as e:
        print(e)
        return redirect(url_for('index'))


if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port='5000')