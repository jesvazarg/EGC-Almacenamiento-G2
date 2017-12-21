from database import *

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