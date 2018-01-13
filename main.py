#encoding: UTF-8
import ast

from flask import Flask, json, jsonify
from flask_restful import Api, reqparse
from werkzeug.exceptions import NotFound, BadRequest, Unauthorized

from database import *
from cifrado_aes import *
from _mysql_exceptions import IntegrityError

import warnings
warnings.filterwarnings("ignore", "Unknown table.*")
warnings.filterwarnings("ignore", message = "Changing sql mode 'NO_AUTO_CREATE_USER' is deprecated. It will be removed in a future release.")

app = Flask(__name__)
api = Api(app)
key = 'Almacen de votos'

# ERRORES

@app.errorhandler(NotFound)
def handle_not_found(error=None):
    if not error:
        error = "Not Found."
    return error, 404


@app.errorhandler(BadRequest)
def handle_bad_request(error=None):
    if not error:
        error = "Bad request."
    return error, 400


@app.errorhandler(Unauthorized)
def handle_unauthorized(error=None):
    if not error:
        error = "Unauthorized."
    return error, 401


# GET

@app.route('/get/comprobar_voto/<token_bd>/<token_usuario>/<token_votacion>', methods=['GET'])
def comprobar_voto(token_bd, token_usuario, token_votacion):
    db = conectar_db()

    if not comprobar_token(db, token_bd):
        return handle_unauthorized('Token incorrecto.')

    votes = get_voto(db, token_usuario, token_votacion)

    if len(votes) == 0:
        desconectar_db(db)
        return handle_not_found('El usuario no ha realizado ningun voto en esta votacion.')
    else:
        desconectar_db(db)

        result = json.dumps(votes)
        return result


@app.route('/get/comprobar_voto_pregunta/<token_bd>/<token_usuario>/<token_votacion>/<token_pregunta>', methods=['GET'])
def comprobar_voto_pregunta(token_bd, token_usuario, token_votacion, token_pregunta):
    db = conectar_db()

    if not comprobar_token(db, token_bd):
        return handle_unauthorized('Token incorrecto.')

    votes = get_voto_pregunta(db, token_usuario, token_votacion, token_pregunta)

    if len(votes) == 0:
        desconectar_db(db)
        return handle_not_found('El usuario no ha realizado ningun voto en esta pregunta de esta votacion.')
    else:
        desconectar_db(db)

        result = json.dumps(votes)
        return result


@app.route('/get/obtener_votos/<token_bd>/<token_votacion>/<token_pregunta>', methods=['GET'])
def obtener_votos(token_bd, token_votacion, token_pregunta):
    db = conectar_db()

    if not comprobar_token(db, token_bd):
        return handle_unauthorized('Token incorrecto.')

    votes = consultar_votos_pregunta(db, token_pregunta, token_votacion)

    desconectar_db(db)

    votes = json.dumps(votes)
    return votes

# POST

parser = reqparse.RequestParser()
parser.add_argument('token_bd')
parser.add_argument('token_usuario')
parser.add_argument('token_votacion')
parser.add_argument('token_pregunta')
parser.add_argument('token_respuesta')
parser.add_argument('token_voto')


@app.route('/post/almacenar_voto', methods=['POST'])
def almacenar_voto():
    args = parser.parse_args()

    token_bd = args['token_bd']

    usuario_id = args['token_usuario']
    votacion_id = args['token_votacion']

    pregunta_id = args['token_pregunta']

    respuesta_id = args['token_respuesta']
    respuesta_id = encrypt(respuesta_id,key)

    db = conectar_db()

    if not comprobar_token(db, token_bd):
        return handle_unauthorized('Token incorrecto.')

    try:
        guardar_voto(db, usuario_id, votacion_id, pregunta_id, respuesta_id)
    except IntegrityError:
        desconectar_db(db)
        return handle_bad_request("Un usuario sólo puede votar una vez a una pregunta.")
    else:
        desconectar_db(db)
        return json.dumps({"message": "El voto se ha almacenado satisfactoriamente."})


@app.route('/post/almacenar_voto_multiple', methods=['POST'])
def almacenar_voto_multiple():
    args = parser.parse_args()

    token_bd = args['token_bd']
    usuario_id = args['token_usuario']

    votacion_id = args['token_votacion']

    array_votos = args['token_voto']

    array_votos = ast.literal_eval(array_votos)

    db = conectar_db()

    if not comprobar_token(db, token_bd):
        return handle_unauthorized('Token incorrecto.')

    for k, v in array_votos.items():
        pregunta_token = v['token_pregunta']

        respuesta_token = v['token_respuesta']
        respuesta_token = encrypt(respuesta_token,key)

        try:
            guardar_voto(db, usuario_id, votacion_id, pregunta_token, respuesta_token)
        except IntegrityError:
            desconectar_db(db)
            return handle_bad_request("Un usuario solo puede votar una vez a una pregunta.")
    desconectar_db(db)
    return json.dumps({"message": "El voto se ha almacenado satisfactoriamente."})


if __name__ == '__main__':
    dbCreada = False
    db = MySQLdb.connect(host="127.0.0.1", user="root", passwd="root")
    cursor = db.cursor()
    cursor.execute("show databases")
    for x in cursor.fetchall():
        if x[0] == "almacenamiento":
            dbCreada = True
    if dbCreada == False:
        ejecutar_script_archivo('almacenamiento-votos.sql')
    db.close()

    app.run(debug=True)