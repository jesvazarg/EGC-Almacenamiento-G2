from database import *

if __name__ == '__main__':
    db = conectar_db()

    prueba_positiva = get_voto(db, "1", "1") # Prueba positiva
    print prueba_positiva

    prueba_negativa = get_voto(db, "123", "1") # Error, no existe el token
    print prueba_negativa
