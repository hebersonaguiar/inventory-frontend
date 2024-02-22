import json, re, csv, requests
from flask import Flask, render_template, request, redirect, url_for, flash, stream_with_context, g, session
from flask_restful import Resource, Api
# from flask_mysqldb import MySQL
from flask_cors import CORS
from flask_jsonpify import jsonify
from json import dumps
from datetime import datetime

app = Flask(__name__)
api = Api(app)
CORS(app, resources={r"/*": {"origins": "*"}})
app.secret_key = "flash message"


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/servers', methods=['GET'])
def servers():
	# if g.username:
    try:

        api_url = "http://inventory:5000/hosts"
        response = requests.get(api_url)
        # print(response.json())

        # cur = mysql.connection.cursor()
        # cur.execute("SELECT * FROM users")
        # data = cur.fetchall()
        # cur.close()

        # user = g.username

        # domain_name = 'mdh.gov.br'
        # domain      = domain_name.split('.')
        # connect     = conn()

        # connect.search('dc={},dc={},dc={}'.format(domain[0], domain[1], domain[2]), '(sAMAccountName={})'.format(user), attributes = [ 'sAMAccountName', 'distinguishedName', 'displayName'], search_scope=SUBTREE )

        # displayNameObj  = connect.entries[0].displayName.value
        # displayName = str(displayNameObj)

        data = json.load(response.json)

        print(data)

        return render_template('servers.html', hosts=data)
        # return response.json()

    except Exception as e:
        # return redirect(url_for('servers'))
        return redirect(url_for('index'))

	# return redirect(url_for('servers'))

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port='5000')