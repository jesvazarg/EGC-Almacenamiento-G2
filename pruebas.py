#encoding:UTF-8
from database import *
import requests

if __name__ == '__main__':
    db = conectar_db()

    # Pruebas para el metodo get_voto

    prueba_positiva = get_voto(db, "1", "1") # Prueba positiva
    print prueba_positiva

    prueba_negativa1 = get_voto(db, "123", "1") # Prueba negativa, no existe el token_usuario
    print prueba_negativa1

    prueba_negativa = get_voto(db, "1", "123")  # Prueba negativa, no existe el token_votacion
    print prueba_negativa

    # Pruebas para el metodo get_voto_pregunta

    prueba_positiva = get_voto_pregunta(db, "1", "1", "1")  # Prueba positiva
    print prueba_positiva

    prueba_negativa1 = get_voto_pregunta(db, "123", "1", "1")  # Prueba negativa, no existe el token_usuario
    print prueba_negativa1

    prueba_negativa2 = get_voto_pregunta(db, "1", "123", "1")  # Prueba negativa, no existe el token_votacion
    print prueba_negativa2

    prueba_negativa3 = get_voto_pregunta(db, "1", "1", "123")  # Prueba negativa, no existe el token_pregunta
    print prueba_negativa3

    # Pruebas para el metodo comprobar_token

    prueba_positiva = comprobar_token(db, "12345QWERTY")  # Prueba positiva
    print prueba_positiva

    prueba_negativa1 = comprobar_token(db, "123")  # Prueba negativa, no existe el token
    print prueba_negativa1

    # Pruebas para el metodo obtener_votos

    prueba_positiva = get_voto(db, "1", "1")  # Prueba positiva
    print prueba_positiva

    prueba_negativa = get_voto(db, "123", "1")  # Error, no existe el token
    print prueba_negativa

    # Pruebas para el metodo almacenar_votos

    prueba_positiva = get_voto(db, "1", "1")  # Prueba positiva
    print prueba_positiva

    prueba_negativa = get_voto(db, "123", "1")  # Error, no existe el token
    print prueba_negativa


    # Pruebas para el metodo comprobar voto

    comprobar_voto = requests.get("http://127.0.0.1:5000/get/comprobar_voto/QWERTY12345/1/1")
    comprobar_voto_sin_token = requests.get("http://127.0.0.1:5000/get/comprobar_voto/1/1/1")
    comprobar_voto_respuesta_vacia = requests.get("http://127.0.0.1:5000/get/comprobar_voto/QWERTY12345/19/1")

    print "Comprobar voto (Llamada Correcta)"

    print comprobar_voto
    print comprobar_voto.text

    print "Comprobar voto (Sin token)"

    print comprobar_voto_sin_token
    print comprobar_voto_sin_token.text

    print "Comprobar voto (Respuesta vacia)"

    print comprobar_voto_respuesta_vacia
    print comprobar_voto_respuesta_vacia.text

    # Pruebas para el metodo comprobar voto pregunta

    comprobar_voto_pregunta = requests.get("http://127.0.0.1:5000/get/comprobar_voto_pregunta/QWERTY12345/1/1/1")
    comprobar_voto_pregunta_sin_token = requests.get("http://127.0.0.1:5000/get/comprobar_voto_pregunta/1/1/1/1")
    comprobar_voto_pregunta_respuesta_vacia = requests.get("http://127.0.0.1:5000/get/comprobar_voto_pregunta/QWERTY12345/19/1/1")

    print "Comprobar voto pregunta (Llamada Correcta)"

    print comprobar_voto_pregunta
    print comprobar_voto_pregunta.text

    print "Comprobar voto pregunta (Sin token)"

    print comprobar_voto_pregunta_sin_token
    print comprobar_voto_pregunta_sin_token.text

    print "Comprobar voto pregunta (Respuesta vacía)"

    print comprobar_voto_pregunta_respuesta_vacia
    print comprobar_voto_pregunta_respuesta_vacia.text








