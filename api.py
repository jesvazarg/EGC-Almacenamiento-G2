#encoding: UTF-8
from flask import Flask, request
from flask_restful import Resource, Api, reqparse, abort
from database import *
from _mysql_exceptions import IntegrityError

app = Flask(__name__)
api = Api(app)


# GET


class ComprobarVoto(Resource):
    def get(self, usuario_id):
        db = conectar_db()

        votes = comprobar_voto(db, usuario_id)

        desconectar_db(db)
        return votes


class ObtenerVotos(Resource):
    def get(self, token, pregunta_id):
        db = conectar_db()

        # TODO: Aqui hacemos las comprobaciones del token

        votes = consultar_votos_pregunta(db, pregunta_id)

        desconectar_db(db)

        return votes

# POST

# Parámetros para el POST
parser = reqparse.RequestParser()
parser.add_argument('usuario_id')
parser.add_argument('pregunta_id')
parser.add_argument('respuesta_id')


class AlmacenarVoto(Resource):
    def post(self):
        args = parser.parse_args()
        try:
            db = conectar_db()

            almacenar_voto(db, args['usuario_id'], args['pregunta_id'], args['respuesta_id'])

            desconectar_db(db)
        except IntegrityError:
            abort(400, message="Un usuario sólo puede votar una vez a una pregunta.")
        else:
            return {"message": "El voto se ha almacenado satisfactoriamente."}

# URLs api

api.add_resource(ComprobarVoto, "/get/comprobar_voto/<int:usuario_id>")
api.add_resource(ObtenerVotos, "/get/obtener_votos/<int:token>/<int:pregunta_id>")
api.add_resource(AlmacenarVoto, "/post/almacenar_voto")

if __name__ == '__main__':
    app.run(debug=True)
