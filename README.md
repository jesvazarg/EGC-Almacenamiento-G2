# Almacenamiento de votos
Repositorio para el módulo de almacenamiento de votos de la asignatura EGC 17/18.
	
Manual de instalación:

1. Instalar PyCharm.

	https://www.lifewire.com/how-to-install-the-pycharm-python-ide-in-linux-4091033 
	(Instrucciones para instalar PyCharm en Linux)

2. Instalar Python y git:
	
	sudo apt-get install python2.7
	sudo apt-get install git (alternativa: sudo apt-get install git-all)

3. Instalar MySQL Community Server 5.7.19:

	- Acceder a https://dev.mysql.com/downloads/mysql/ y descargar la version correspondiente.

	- Descomprimir e instalar (la contraseña de root debe ser root).

	- Una vez instalado, abrir la terminal y escribir "sudo su mysql -uroot -proot".

	- Dentro de mysql, se crea la base de datos mediante el siguiente comando:

	"create database almacenamiento"

	- Una vez creada, se selecciona la base de datos "almacenamiento" mediante el siguiente comando:

	"use almacenamiento"

	- Finalmente, usando el script SQL proporcionado, se pega el contenido en la terminal para crear las tablas necesarias automáticamente.

4. Instalar el gestor de paquetes pip para Python:

	sudo apt-get install python-pip python-dev build-essential
	sudo pip install --upgrade pip
	sudo pip install --upgrade virtualenv

5. Para instalar automáticamente las librerias necesarias, utilizar el siguiente comando:

	"pip install -r requirements.txt"

6. Para comprobar el funcionamiento de la API se puede usar, por ejemplo:
	
	- Postman:

	Comandos para instalar Postman en Linux:

	wget https://dl.pstmn.io/download/latest/linux64 -O postman.tar.gz
	sudo tar -xzf postman.tar.gz -C /opt
	rm postman.tar.gz
	sudo ln -s /opt/Postman/Postman /usr/bin/postman


	- RESTClient:

	Instalar la siguiente extensión de Firefox:

	https://addons.mozilla.org/es/firefox/addon/restclient/


** Nota: Los comandos para comprobar si mysql esta activo y activarlo o desactivarlo son:

        service mysqld status
        service mysqld stop
        service mysqld start

** Nota2: Si no se puede conectar la api seguir los pasos de la pagina:

	http://www.zyxware.com/articles/5539/solved-cant-connect-to-local-mysql-server-through-socket-var-run-mysqld-mysqld-sock

	
