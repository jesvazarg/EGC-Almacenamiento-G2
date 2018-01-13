from Crypto.Cipher import AES
from Crypto import Random
import base64


def pad(s): #Esto rellena de caracteres hasta que haya un multiplo de 16,24 o 32 caracteres
    return s + (AES.block_size - len(s) % AES.block_size) * chr(AES.block_size - len(s) % AES.block_size)

def unpad(s): #Realiza la accion de pad a la inversa eliminando los acaracteres que no pertenecen al texto claro
    return s[:-ord(s[len(s)-1:])]

def encrypt(texto_claro,key):
    texto_claro = pad(texto_claro)
    iv = Random.new().read(AES.block_size) #texto aleatorio que se anyade por seguridad
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return base64.b64encode(iv + cipher.encrypt(texto_claro)) #Convierte los caracteres a caracteres base64

def decrypt(texto_encriptado,key):
    texto_encriptado = base64.b64decode(texto_encriptado)
    iv = texto_encriptado[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(texto_encriptado[AES.block_size:])).decode('utf-8')



key = "Almacen de votos"
test = "25"

# print (encrypt(test,key))