#encoding: UTF-8
from flask import Flask, request
from flask_restful import Resource, Api, reqparse, abort
from database import *
from _mysql_exceptions import IntegrityError

app = Flask(__name__)
api = Api(app)


# GET


class ComprobarVoto(Resource):
    def get(self, usuario_id, votacion_id):
        db = conectar_db()

        votes = comprobar_voto(db, usuario_id, votacion_id)
        print len(votes)

        if len(votes) == 0:
            abort(404, message="El usuario no ha realizado ningun voto en esta votacion.")
        else:
            result = []
            for row in votes:
                result.append({
                    "voto_id": row[0],
                    "usuario_id": row[1],
                    "votacion_id": row[2],
                    "pregunta_id": row[3],
                    "respuesta_id": row[4],
                })
            desconectar_db(db)
            return result


class ComprobarVotoPregunta(Resource):
    def get(self, usuario_id, votacion_id, pregunta_id):
        db = conectar_db()

        votes = comprobar_voto_pregunta(db, usuario_id, votacion_id, pregunta_id)
        print len(votes)

        if len(votes) == 0:
            abort(404, message="El usuario no ha realizado ningun voto en esta pregunta de esta votacion.")
        else:
            result = []
            for row in votes:
                result.append({
                    "voto_id": row[0],
                    "usuario_id": row[1],
                    "votacion_id": row[2],
                    "pregunta_id": row[3],
                    "respuesta_id": row[4],
                })
            desconectar_db(db)
            return result


class ObtenerVotos(Resource):
    def get(self, token, pregunta_id, votacion_id):
        db = conectar_db()

        # TODO: Aqui hacemos las comprobaciones del token

        votes = consultar_votos_pregunta(db, pregunta_id, votacion_id)

        desconectar_db(db)

        return votes

# POST

# Parámetros para el POST
parser = reqparse.RequestParser()
parser.add_argument('usuario_id')
parser.add_argument('pregunta_id')
parser.add_argument('respuesta_id')
parser.add_argument('votacion_id')


class AlmacenarVoto(Resource):
    def post(self):
        args = parser.parse_args()
        try:
            db = conectar_db()

            almacenar_voto(db, args['usuario_id'], args['pregunta_id'], args['respuesta_id'], args['votacion_id'])

            desconectar_db(db)
        except IntegrityError:
            abort(400, message="Un usuario sólo puede votar una vez a una pregunta.")
        else:
            return {"message": "El voto se ha almacenado satisfactoriamente."}

# URLs api

api.add_resource(ComprobarVoto, "/get/comprobar_voto/<int:usuario_id>/<int:votacion_id>")
api.add_resource(ComprobarVotoPregunta, "/get/comprobar_voto_pregunta/<int:usuario_id>/<int:votacion_id>/<int:pregunta_id>")
api.add_resource(ObtenerVotos, "/get/obtener_votos/<int:token>/<int:pregunta_id>/<int:votacion_id>")
api.add_resource(AlmacenarVoto, "/post/almacenar_voto")

if __name__ == '__main__':
    app.run(debug=True)
