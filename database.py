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
    result = []

    cursor.execute("SELECT * FROM votos WHERE usuario_id=%(usuario_id)s and votacion_id=%(votacion_id)s",
                   {'usuario_id': usuario_id, 'votacion_id': votacion_id})

    for row in cursor.fetchall():
        result.append({
            "voto_id": row[0],
            "usuario_id": row[1],
            "pregunta_id": row[2],
            "respuesta_id": row[3],
            "votacion_id": row[4],
        })

    return result


def consultar_votos_pregunta(db, pregunta_id, votacion_id):
    cursor = db.cursor()
    result = []

    cursor.execute("SELECT * FROM votos WHERE pregunta_id=%(question_id)s and pregunta_id=%(question_id)s",
                   {'question_id': pregunta_id, 'votacion_id': votacion_id})

    for row in cursor.fetchall():
        result.append({
            "voto_id": row[0],
            "usuario_id": row[1],
            "pregunta_id": row[2],
            "respuesta_id": row[3],
            "votacion_id": row[4],
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


def primera_insercion():

    db = conectar_db()

    # you must create a Cursor object. It will let
    #  you execute all the queries you need
    cur = db.cursor()

    add_vote = "INSERT INTO votos (usuario_id, pregunta_id, respuesta_id, votacion_id) VALUES (%s, %s, %s, %s)"
    data_vote1 = (1, 1, 1, 1)
    data_vote2 = (1, 2, 2, 1)
    data_vote3 = (2, 1, 2, 1)
    data_vote4 = (2, 2, 2, 1)
    data_vote5 = (3, 1, 2, 1)
    data_vote6 = (3, 2, 1, 1)
    data_vote7 = (4, 1, None, 1)
    data_vote8 = (5, 2, None, 1)

    # Insert new employee
    cur.execute(add_vote, data_vote1)
    # vote1_no = cur.lastrowid # Para saber la id de la ultima insercion

    cur.execute(add_vote, data_vote2)
    cur.execute(add_vote, data_vote3)
    cur.execute(add_vote, data_vote4)
    cur.execute(add_vote, data_vote5)
    cur.execute(add_vote, data_vote6)
    cur.execute(add_vote, data_vote7)
    cur.execute(add_vote, data_vote8)

    db.commit()

    # Use all the SQL you like
    cur.execute("SELECT * FROM votos")

    # print all the first cell of all the rows
    for row in cur.fetchall():
        print row[0]

    desconectar_db(db)
