#encoding:UTF-8
from database import *
import requests

if __name__ == '__main__':
    db = conectar_db()

    # Pruebas para el metodo get_voto

    print "get voto (Prueba positiva)"

    prueba_positiva = get_voto(db, "1", "1") # Prueba positiva
    print prueba_positiva

    print "get voto (Prueba negativa, no existe el token_usuario)"

    prueba_negativa1 = get_voto(db, "123", "1") # Prueba negativa, no existe el token_usuario
    print prueba_negativa1

    print "get voto (Prueba negativa, no existe el token_votacion)"

    prueba_negativa = get_voto(db, "1", "123")  # Prueba negativa, no existe el token_votacion
    print prueba_negativa

    # Pruebas para el metodo get_voto_pregunta

    print "------------------------------------------"
    print "get voto pregunta (Prueba positiva)"

    prueba_positiva = get_voto_pregunta(db, "1", "1", "1")  # Prueba positiva
    print prueba_positiva

    print "get voto pregunta (Prueba negativa, no existe el token_usuario)"

    prueba_negativa1 = get_voto_pregunta(db, "123", "1", "1")  # Prueba negativa, no existe el token_usuario
    print prueba_negativa1

    print "get voto pregunta (Prueba negativa, no existe el token_votacion)"

    prueba_negativa2 = get_voto_pregunta(db, "1", "123", "1")  # Prueba negativa, no existe el token_votacion
    print prueba_negativa2

    print "get voto pregunta (Prueba negativa, no existe el token_pregunta)"

    prueba_negativa3 = get_voto_pregunta(db, "1", "1", "123")  # Prueba negativa, no existe el token_pregunta
    print prueba_negativa3

    # Pruebas para el metodo comprobar_token

    print "------------------------------------------"
    print "comprobar token (Prueba positiva)"

    prueba_positiva = comprobar_token(db, "12345QWERTY")  # Prueba positiva
    print prueba_positiva

    print "comprobar token (Prueba negativa, no existe el token)"

    prueba_negativa1 = comprobar_token(db, "123")  # Prueba negativa, no existe el token
    print prueba_negativa1

    # Pruebas para el metodo obtener_votos

    obtener_voto = requests.get("http://localhost:5000/get/obtener_votos/QWERTY12345/1/1")
    obtener_voto_token_incorrecto = requests.get("http://localhost:5000/get/obtener_votos/DFKJGE54368/1/1")
    obtener_voto_votacion_incorrecta = requests.get("http://localhost:5000/get/obtener_votos/QWERTY12345/78/1")

    print "------------------------------------------"
    print "Obtener voto (Llamada Correcta)"

    print obtener_voto
    print obtener_voto.text

    print "Obtener voto (Token incorrecto)"

    print obtener_voto_token_incorrecto
    print obtener_voto_token_incorrecto.text

    print "Obtener voto (Respuesta vacia)"

    print obtener_voto_votacion_incorrecta
    print obtener_voto_votacion_incorrecta.text

    # Pruebas para el metodo almacenar_votos

    almacenar_voto = requests.post("http://localhost:5000/post/almacenar_voto", {"token_bd":"QWERTY12345","token_usuario":"25","token_votacion":"1","token_pregunta":"2","token_respuesta":"1"})
    almacenar_voto_token_incorrecto = requests.post("http://localhost:5000/post/almacenar_voto", {"token_bd":"FDAIFJ52987","token_usuario":"26","token_votacion":"1","token_pregunta":"2","token_respuesta":"1"})
    almacenar_voto_repetido = requests.post("http://localhost:5000/post/almacenar_voto", {"token_bd":"QWERTY12345","token_usuario":"1","token_votacion":"1","token_pregunta":"2","token_respuesta":"1"})

    print "------------------------------------------"
    print "Almacenar voto (Llamada Correcta)"

    print almacenar_voto
    print almacenar_voto.text

    print "Almacenar voto (Token incorrecto)"

    print almacenar_voto_token_incorrecto
    print almacenar_voto_token_incorrecto.text

    print "Almacenar voto (Respuesta vacia)"

    print almacenar_voto_repetido
    print almacenar_voto_repetido.text


    # Pruebas para el metodo comprobar voto

    comprobar_voto = requests.get("http://127.0.0.1:5000/get/comprobar_voto/QWERTY12345/1/1")
    comprobar_voto_token_incorrecto = requests.get("http://127.0.0.1:5000/get/comprobar_voto/GFJLEO54302/1/1/1")
    comprobar_voto_respuesta_vacia = requests.get("http://127.0.0.1:5000/get/comprobar_voto/QWERTY12345/19/1")

    print "------------------------------------------"
    print "Comprobar voto (Llamada Correcta)"

    print comprobar_voto
    print comprobar_voto.text

    print "Comprobar voto (Token incorrecto)"

    print comprobar_voto_token_incorrecto
    print comprobar_voto_token_incorrecto.text

    print "Comprobar voto (Respuesta vacia)"

    print comprobar_voto_respuesta_vacia
    print comprobar_voto_respuesta_vacia.text

    # Pruebas para el metodo comprobar voto pregunta

    comprobar_voto_pregunta = requests.get("http://127.0.0.1:5000/get/comprobar_voto_pregunta/QWERTY12345/1/1/1")
    comprobar_voto_pregunta_token_incorrecto = requests.get("http://127.0.0.1:5000/get/comprobar_voto_pregunta/DGLQNF54932/1/1/1/1")
    comprobar_voto_pregunta_respuesta_vacia = requests.get("http://127.0.0.1:5000/get/comprobar_voto_pregunta/QWERTY12345/19/1/1")

    print "------------------------------------------"
    print "Comprobar voto pregunta (Llamada Correcta)"

    print comprobar_voto_pregunta
    print comprobar_voto_pregunta.text

    print "Comprobar voto pregunta (Token incorrecto)"

    print comprobar_voto_pregunta_token_incorrecto
    print comprobar_voto_pregunta_token_incorrecto.text

    print "Comprobar voto pregunta (Respuesta vacía)"

    print comprobar_voto_pregunta_respuesta_vacia
    print comprobar_voto_pregunta_respuesta_vacia.text

    # Pruebas para el metodo consultar_votos_pregunta

    print "------------------------------------------"
    print "Consultar voto pregunta"

    prueba_positiva = consultar_votos_pregunta(db, "1", "1")  # Prueba positiva
    print prueba_positiva

    print "Consultar voto pregunta (Respuesta vacía)"

    prueba_negativa = consultar_votos_pregunta(db, "123", "1")  # Error, no existe el token
    print prueba_negativa

    # Pruebas para el metodo guardar_voto

    print "------------------------------------------"
    print "Guardar voto"

    prueba_positiva = guardar_voto(db,"1", "1", "6", "3")  # Prueba positiva
    print prueba_positiva

    print "Guardar voto (Respuesta vacía)"

    prueba_negativa = guardar_voto(db, "1", "1", "1", "1")  # Error, ya existe el token
    print prueba_negativa