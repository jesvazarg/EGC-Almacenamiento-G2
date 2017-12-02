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


def comprobar_voto(db, usuario_id, votacion_id):
    cursor = db.cursor()

    cursor.execute("SELECT * FROM votos WHERE usuario_id=%(usuario_id)s and votacion_id=%(votacion_id)s",
                   {'usuario_id': usuario_id, 'votacion_id': votacion_id})

    return cursor.fetchall()


def comprobar_voto_pregunta(db, usuario_id, votacion_id, pregunta_id):
    cursor = db.cursor()

    cursor.execute("SELECT * FROM votos WHERE usuario_id=%(usuario_id)s and votacion_id=%(votacion_id)s and pregunta_id=%(pregunta_id)s",
                   {'usuario_id': usuario_id, 'votacion_id': votacion_id, 'pregunta_id': pregunta_id})

    return cursor.fetchall()


def consultar_votos_pregunta(db, pregunta_id, votacion_id):
    cursor = db.cursor()
    result = []

    cursor.execute("SELECT * FROM votos WHERE pregunta_id=%(question_id)s and pregunta_id=%(question_id)s",
                   {'question_id': pregunta_id, 'votacion_id': votacion_id})

    for row in cursor.fetchall():
        result.append({
            "voto_id": row[0],
            "usuario_id": row[1],
            "votacion_id": row[2],
            "pregunta_id": row[3],
            "respuesta_id": row[4],
        })

    return result

# Inserción


def almacenar_voto(db, usuario_id, pregunta_id, respuesta_id, votacion_id):
    cursor = db.cursor()
    result = []

    add_vote = "INSERT INTO votos (usuario_id, pregunta_id, respuesta_id, votacion_id) VALUES (%s, %s, %s, %s)"
    data_vote1 = (usuario_id, pregunta_id, respuesta_id, votacion_id)
    cursor.execute(add_vote, data_vote1)

    db.commit()

    return result