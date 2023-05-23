from flask import Flask, jsonify
from flask_restful import Api, Resource


app = Flask(__name__)
api = Api(app)


class Apresentacao(Resource):
    def get(self):
        return jsonify("Bem vindo a pior API da história")


class CPFLOcorrencia(Resource):
    def get(self):
        data = get_data
        return jsonify(data)


class CPFLArrecadacao(Resource):
    def get(self):
        return {'id': 2}


api.add_resource(Apresentacao, '/')
api.add_resource(CPFLOcorrencia, '/cpfl/ocorrencia')
api.add_resource(CPFLArrecadacao, '/cpfl/arrecadacao')


if __name__ == '__main__':
    app.run(debug=True)
"""
from flask import Flask
from flask_restful import Api
from config import Config
from models import mysql
from controllers import Users

app = Flask(__name__)
app.config.from_object(Config)
mysql.init_app(app)
api = Api(app)

api.add_resource(Users, '/users')

if __name__ == '__main__':
    app.run(debug=True)

if __name__ == '__main__':
    app.run(debug=True)

"""