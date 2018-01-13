#encoding:UTF-8
from database import *
import requests
from _mysql_exceptions import IntegrityError
from random import randint

if __name__ == '__main__':
    db = conectar_db()

    print "========================================================="
    print "PRUEBA 1: Comprobar voto (Funcional)"
    print "========================================================="

    print "Comprobar voto: PRUEBA 1.1 (Llamada Correcta)"
    prueba_positiva = requests.get("http://127.0.0.1:5000/get/comprobar_voto/QWERTY12345/1/1")
    print "Resultado Esperado: Array con los datos de los votos realizados por el usuario con token=1"
    print "Resultado Obtenido: " + str(prueba_positiva) + str(prueba_positiva.text)
    if str(prueba_positiva) == '<Response [404]>':
        print "---------------------------------------------------------"
        print "INCORRECTO"
    else:
        print "-------------------------------------------------------------"
        print "CORRECTO"

    print "---------------------------------------------------------"
    print "Comprobar voto: PRUEBA 1.2 (Token incorrecto)"
    prueba_negativa1 = requests.get("http://127.0.0.1:5000/get/comprobar_voto/1/1/1")
    print "Resultado Esperado: <Response [401]>Token incorrecto."
    print "Resultado Obtenido: " + str(prueba_negativa1) + str(prueba_negativa1.text)
    if str(prueba_negativa1) + str(prueba_negativa1.text) == "<Response [401]>Token incorrecto.":
        print "---------------------------------------------------------"
        print "CORRECTO"
    else:
        print "---------------------------------------------------------"
        print "INCORRECTO"

    print "---------------------------------------------------------"
    print "Comprobar voto: PRUEBA 1.3 (Respuesta vacía)"
    prueba_negativa2 = requests.get("http://127.0.0.1:5000/get/comprobar_voto/QWERTY12345/19/1")
    print "Resultado Esperado: <Response [404]>El usuario no ha realizado ningun voto en esta votacion."
    print "Resultado Obtenido: " + str(prueba_negativa2) + str(prueba_negativa2.text)
    if str(prueba_negativa2) + str(prueba_negativa2.text) == "<Response [404]>El usuario no ha realizado ningun voto en esta votacion.":
        print "---------------------------------------------------------"
        print "CORRECTO"
    else:
        print "---------------------------------------------------------"
        print "INCORRECTO"

    print "---------------------------------------------------------"

    print "========================================================="
    print "PRUEBA 2: Comprobar voto pregunta (Funcional)"
    print "========================================================="

    print "Comprobar voto pregunta: PRUEBA 2.1 (Llamada Correcta)"
    prueba_positiva = requests.get("http://127.0.0.1:5000/get/comprobar_voto_pregunta/QWERTY12345/1/1/1")
    print "Resultado Esperado: Array con los datos de los votos realizados por el usuario con token=1 en la pregunta con token=1"
    print "Resultado Obtenido: " + str(prueba_positiva) + str(prueba_positiva.text)
    if str(prueba_positiva) == '<Response [404]>':
        print "---------------------------------------------------------"
        print "INCORRECTO"
    else:
        print "-------------------------------------------------------------"
        print "CORRECTO"

    print "---------------------------------------------------------"
    print "Comprobar voto pregunta: PRUEBA 2.2 (Token incorrecto)"
    prueba_negativa1 = requests.get("http://127.0.0.1:5000/get/comprobar_voto_pregunta/1/1/1/1")
    print "Resultado Esperado: <Response [401]>Token incorrecto."
    print "Resultado Obtenido: " + str(prueba_negativa1) + str(prueba_negativa1.text)
    if str(prueba_negativa1) + str(prueba_negativa1.text) == "<Response [401]>Token incorrecto.":
        print "---------------------------------------------------------"
        print "CORRECTO"
    else:
        print "---------------------------------------------------------"
        print "INCORRECTO"

    print "---------------------------------------------------------"
    print "Comprobar voto pregunta: PRUEBA 2.3 (Respuesta vacía)"
    prueba_negativa2 = requests.get("http://127.0.0.1:5000/get/comprobar_voto_pregunta/QWERTY12345/19/1/1")
    print "Resultado Esperado: <Response [404]>El usuario no ha realizado ningun voto en esta pregunta de esta votacion."
    print "Resultado Obtenido: " + str(prueba_negativa2) + str(prueba_negativa2.text)
    if str(prueba_negativa2) + str(prueba_negativa2.text) == "<Response [404]>El usuario no ha realizado ningun voto en esta pregunta de esta votacion.":
        print "---------------------------------------------------------"
        print "CORRECTO"
    else:
        print "---------------------------------------------------------"
        print "INCORRECTO"

    print "---------------------------------------------------------"

    print "========================================================="
    print "PRUEBA 3: Comprobar token (Unitaria)"
    print "========================================================="

    print "Comprobar token: PRUEBA 3.1 (Llamada correcta)"
    prueba_positiva = comprobar_token(db, "12345QWERTY")  # Prueba positiva
    print "Resultado Esperado: True"
    print "Resultado Obtenido: " + str(prueba_positiva)
    if str(prueba_positiva) == "True":
        print "---------------------------------------------------------"
        print "CORRECTO"
    else:
        print "---------------------------------------------------------"
        print "INCORRECTO"

    print "---------------------------------------------------------"
    print "Comprobar token: PRUEBA 3.2 (Prueba negativa, no existe el token)"
    prueba_negativa1 = comprobar_token(db, "123")  # Prueba negativa, no existe el token
    print "Resultado Esperado: False"
    print "Resultado Obtenido: " + str(prueba_negativa1)
    if str(prueba_negativa1) == "False":
        print "---------------------------------------------------------"
        print "CORRECTO"
    else:
        print "---------------------------------------------------------"
        print "INCORRECTO"

    print "---------------------------------------------------------"

    print "========================================================="
    print "PRUEBA 4: Get voto (Unitaria)"
    print "========================================================="

    print "Get voto: PRUEBA 4.1 (Llamada correcta)"
    prueba_positiva = get_voto(db, "1", "1") # Prueba positiva
    print "Resultado Esperado: Array con los datos de los votos realizados por el usuario a la votación dada"
    print "Resultado Obtenido: " + str(prueba_positiva)
    if str(prueba_positiva) == '<Response [404]>':
        print "---------------------------------------------------------"
        print "INCORRECTO"
    else:
        print "-------------------------------------------------------------"
        print "CORRECTO"

    print "---------------------------------------------------------"
    print "Get voto: PRUEBA 4.2 (No existe token)"
    prueba_negativa1 = get_voto(db, "123", "1") # Prueba negativa, no existe el token_usuario
    print "Resultado Esperado: Array vacío"
    print "Resultado Obtenido: " + str(prueba_negativa1)
    if str(prueba_negativa1) == '[]':
        print "---------------------------------------------------------"
        print "CORRECTO"
    else:
        print "---------------------------------------------------------"
        print "INCORRECTO"

    print "---------------------------------------------------------"
    print "Get voto: PRUEBA 4.3 (No existe token_votacion)"
    prueba_negativa2 = get_voto(db, "1", "123")  # Prueba negativa, no existe el token_votacion
    print "Resultado Esperado: Array vacío"
    print "Resultado Obtenido: " + str(prueba_negativa2)
    if str(prueba_negativa2) == '[]':
        print "---------------------------------------------------------"
        print "CORRECTO"
    else:
        print "---------------------------------------------------------"
        print "INCORRECTO"

    print "---------------------------------------------------------"

    # Pruebas para el metodo get_voto_pregunta

    print "========================================================="
    print "PRUEBA 5: Get voto pregunta (Unitaria)"
    print "========================================================="

    print "Get voto pregunta: PRUEBA 5.1 (Llamada correcta"
    prueba_positiva = get_voto_pregunta(db, "1", "1", "1")  # Prueba positiva
    print "Resultado esperado: Array con el voto realizado por el usuario para una pregunta de una votación dada"
    print "Resultado Obtenido: " + str(prueba_positiva)
    if str(prueba_positiva) == '[]':
        print "---------------------------------------------------------"
        print "INCORRECTO"
    else:
        print "---------------------------------------------------------"
        print "CORRECTO"

    print "---------------------------------------------------------"
    print "Get voto pregunta: PRUEBA 5.2 (No existe token_usuario)"
    prueba_negativa1 = get_voto_pregunta(db, "123", "1", "1")  # Prueba negativa, no existe el token_usuario
    print "Resultado esperado: Array vacío"
    print "Resultado Obtenido: " + str(prueba_negativa1)
    if str(prueba_negativa1) == '[]':
        print "---------------------------------------------------------"
        print "CORRECTO"
    else:
        print "---------------------------------------------------------"
        print "INCORRECTO"

    print "---------------------------------------------------------"
    print "Get voto pregunta: PRUEBA 5.3 (No existe token_votacion)"
    prueba_negativa2 = get_voto_pregunta(db, "1", "123", "1")  # Prueba negativa, no existe el token_votacion
    print "Resultado esperado: Array vacío"
    print "Resultado Obtenido: " + str(prueba_negativa2)
    if str(prueba_negativa2) == '[]':
        print "---------------------------------------------------------"
        print "CORRECTO"
    else:
        print "---------------------------------------------------------"
        print "INCORRECTO"

    print "---------------------------------------------------------"
    print "Get voto pregunta: PRUEBA 5.4 (Prueba negativa, no existe el token_pregunta)"
    prueba_negativa3 = get_voto_pregunta(db, "1", "1", "123")  # Prueba negativa, no existe el token_pregunta
    print "Resultado esperado: Array vacío"
    print "Resultado Obtenido: " + str(prueba_negativa3)
    if str(prueba_negativa3) == '[]':
        print "---------------------------------------------------------"
        print "CORRECTO"
    else:
        print "---------------------------------------------------------"
        print "INCORRECTO"

    print "---------------------------------------------------------"

    print "========================================================="
    print "PRUEBA 6: Obtener votos (Funcional)"
    print "========================================================="

    print "Obtener votos: PRUEBA 6.1 (Llamada correcta)"
    prueba_positiva = requests.get("http://localhost:5000/get/obtener_votos/QWERTY12345/1/1")
    print "Resultado Esperado: Array con los datos de los votos realizados por el usuario con token=1"
    print "Resultado Obtenido: " + str(prueba_positiva.text)
    if str(prueba_positiva) == '<Response [404]>':
        print "---------------------------------------------------------"
        print "INCORRECTO"
    else:
        print "---------------------------------------------------------"
        print "CORRECTO"

    print "---------------------------------------------------------"
    print "Obtener votos: PRUEBA 6.2 (Token incorrecto)"
    prueba_negativa1 = requests.get("http://localhost:5000/get/obtener_votos/DFKJGE54368/1/1")
    print "Resultado Esperado: <Response [401]>Token incorrecto."
    print "Resultado Obtenido: " + str(prueba_negativa1) + str(prueba_negativa1.text)
    if str(prueba_negativa1) + str(prueba_negativa1.text) == "<Response [401]>Token incorrecto.":
        print "---------------------------------------------------------"
        print "CORRECTO"
    else:
        print "---------------------------------------------------------"
        print "INCORRECTO"

    print "---------------------------------------------------------"
    print "Obtener votos: PRUEBA 6.3 (Array Vacío)"
    prueba_negativa2 = requests.get("http://localhost:5000/get/obtener_votos/QWERTY12345/78/1")
    print "Resultado Esperado: Array vacío"
    print "Resultado Obtenido: " + str(prueba_negativa2) + str(prueba_negativa2.text)
    if str(prueba_negativa2.text) == '[]':
        print "---------------------------------------------------------"
        print "CORRECTO"
    else:
        print "---------------------------------------------------------"
        print "INCORRECTO"
    
    print "---------------------------------------------------------"


    print "========================================================="
    print "PRUEBA 7: Almacenar votos (Funcional)"
    print "========================================================="

    print "Almacenar votos: PRUEBA 7.1 (Llamada Correcta)"
    print "Resultado Esperado: <Response [200]>El voto se ha almacenado satisfactoriamente."
    prueba_positiva = requests.post("http://localhost:5000/post/almacenar_voto", {"token_bd":"QWERTY12345","token_usuario":"28","token_votacion":"1","token_pregunta":"2","token_respuesta":"1"})
    print "Resultado Obtenido: " + str(prueba_positiva) + prueba_positiva.text.encode('utf-8')

    if str(prueba_positiva) == "<Response [200]>":
        print "---------------------------------------------------------"
        print "CORRECTO"
    elif str(prueba_positiva) == "<Response [400]>":
        print "---------------------------------------------------------"
        print "La llamada está bien pero ese voto ya existe y no se puede duplicar"
    else:
        print "---------------------------------------------------------"
        print "CORRECTO"

    print "---------------------------------------------------------"
    print "Almacenar votos: PRUEBA 7.2 (Token Incorrecto)"
    prueba_negativa1 = requests.post("http://localhost:5000/post/almacenar_voto", {"token_bd":"FDAIFJ52987","token_usuario":"26","token_votacion":"1","token_pregunta":"2","token_respuesta":"1"})
    print "Resultado Esperado: <Response [401]>Token incorrecto."
    print "Resultado Obtenido: " + str(prueba_negativa1) + str(prueba_negativa1.text)
    if str(prueba_negativa1) + str(prueba_negativa1.text) == "<Response [401]>Token incorrecto.":
        print "---------------------------------------------------------"
        print "CORRECTO"
    else:
        print "---------------------------------------------------------"
        print "INCORRECTO"

    print "---------------------------------------------------------"
    print "Almacenar votos: PRUEBA 7.3 (Voto repetido)"
    prueba_negativa2 = requests.post("http://localhost:5000/post/almacenar_voto", {"token_bd":"QWERTY12345","token_usuario":"1","token_votacion":"1","token_pregunta":"2","token_respuesta":"1"})
    print "Resultado Esperado: <Response [400]>Un usuario sólo puede votar una vez a una pregunta."
    print "Resultado Obtenido: " + str(prueba_negativa2) + prueba_negativa2.text.encode('utf-8')
    if str(prueba_negativa2) + prueba_negativa2.text.encode('utf-8') == "<Response [400]>Un usuario sólo puede votar una vez a una pregunta.":
        print "---------------------------------------------------------"
        print "CORRECTO"
    else:
        print "---------------------------------------------------------"
        print "INCORRECTO"

    print "---------------------------------------------------------"

    print "========================================================="
    print "PRUEBA 8: Consultar voto pregunta (Unitaria)"
    print "========================================================="

    print "Consultar voto pregunta: PRUEBA 8.1 (Llamada correcta)"
    prueba_positiva = consultar_votos_pregunta(db, "1", "1")  # Prueba positiva
    print "Resultado Esperado: Array con los datos de los votos realizados por el usuario con votación de token=1 y pregunta de token=1"
    print "Resultado Obtenido: " + str(prueba_positiva)
    if str(prueba_positiva) == '<Response [404]>':
        print "---------------------------------------------------------"
        print "INCORRECTO"
    else:
        print "-------------------------------------------------------------"
        print "CORRECTO" 

    print "-------------------------------------------------------------"
    print "Consultar voto pregunta: PRUEBA 8.2 (Respuesta vacía)"
    prueba_negativa = consultar_votos_pregunta(db, "123", "1")  # Error, no existe el token
    print "Resultado Esperado: Array Vacío"
    print "Resultado Obtenido" + str(prueba_negativa)
    if str(prueba_negativa) == '[]':
        print "---------------------------------------------------------"
        print "CORRECTO"
    else:
        print "---------------------------------------------------------"
        print "INCORRECTO"
    
    print "---------------------------------------------------------"

    print "========================================================="
    print "PRUEBA 9: Guardar voto (Unitaria)"
    print "========================================================="
    
    print "Guardar voto: PRUEBA 9.1 (Llamada correcta)"
    print "Resultado Esperado: None"
    try:
        prueba_positiva = guardar_voto(db,"8", "1", "6", "3")  # Prueba positiva
    except IntegrityError:
        print "Resultado Obtenido: " + str(prueba_positiva)
        print "---------------------------------------------------------"
        print "La llamada está bien pero ese voto ya existe y no se puede duplicar"
    else:
        print "Resultado Obtenido: " + str(prueba_positiva)
        if str(prueba_positiva) == "None":
            print "---------------------------------------------------------"
            print "CORRECTO"
        else:
            print "---------------------------------------------------------"
            print "INCORRECTO"

    print "---------------------------------------------------------"
    print "Guardar voto: PRUEBA 9.2 (Respuesta vacía)"
    print "Resultado Esperado: Array vacío (no se puede guardar porque ya existe el token)"
    try:
        prueba_negativa = guardar_voto(db, "1", "1", "1", "1")  # Error, ya existe el token
    except IntegrityError:
        print "Resultado Obtenido: " + str(prueba_negativa)
        print "---------------------------------------------------------"
        print "CORRECTO"
    else:
        print "---------------------------------------------------------"
        print "INCORRECTO"

    print "---------------------------------------------------------"
    

