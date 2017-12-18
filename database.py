#!/usr/bin/python
#encoding:UTF-8
import MySQLdb


def conectar_db():
    db = MySQLdb.connect(host="127.0.0.1",    # your host, usually localhost
                     user="root",         # your username
                     passwd="root",  # your password
                     db="almacenamiento")        # name of the data base
    return db


def desconectar_db(db):
    db.close()

# Consulta


def get_voto(db, usuario_id, votacion_id):
    cursor = db.cursor()
    result = []

    cursor.execute("SELECT * FROM votos WHERE usuario_id=%(usuario_id)s and votacion_id=%(votacion_id)s",
                   {'usuario_id': usuario_id, 'votacion_id': votacion_id})

    for row in cursor.fetchall():
        result.append({
            "id": row[0],
            "token_usuario": row[1],
            "token_votacion": row[2],
            "token_pregunta": row[3],
            "token_respuesta": row[4],
        })

    return result


def get_voto_pregunta(db, usuario_id, votacion_id, pregunta_id):
    cursor = db.cursor()
    result = []

    cursor.execute("SELECT * FROM votos WHERE usuario_id=%(usuario_id)s and votacion_id=%(votacion_id)s and pregunta_id=%(pregunta_id)s",
                   {'usuario_id': usuario_id, 'votacion_id': votacion_id, 'pregunta_id': pregunta_id})

    for row in cursor.fetchall():
        result.append({
            "id": row[0],
            "token_usuario": row[1],
            "token_votacion": row[2],
            "token_pregunta": row[3],
            "token_respuesta": row[4],
        })

    return result


def consultar_votos_pregunta(db, pregunta_id, votacion_id):
    cursor = db.cursor()
    result = []

    cursor.execute("SELECT * FROM votos WHERE pregunta_id=%(question_id)s and pregunta_id=%(question_id)s",
                   {'question_id': pregunta_id, 'votacion_id': votacion_id})

    for row in cursor.fetchall():
        result.append({
            "id": row[0],
            "token_usuario": row[1],
            "token_votacion": row[2],
            "token_pregunta": row[3],
            "token_respuesta": row[4],
        })

    return result

# Inserción


def guardar_voto(db, usuario_id, pregunta_id, respuesta_id, votacion_id):
    cursor = db.cursor()
    result = []

    add_vote = "INSERT INTO votos (usuario_id, pregunta_id, respuesta_id, votacion_id) VALUES (%s, %s, %s, %s)"
    data_vote1 = (usuario_id, pregunta_id, respuesta_id, votacion_id)
    cursor.execute(add_vote, data_vote1)

    db.commit()

    return result