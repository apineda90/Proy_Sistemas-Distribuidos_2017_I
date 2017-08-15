Readme 

Sistemas operativos basados en Debian (Ubuntu, Mint)
RabbitMQ es el broker de mensajes de código abierto más ampliamente implementado.
El servidor rabbitmq está escrito en el lenguaje de programación erlang y se basa en el marco de Open Telecom Platform para la agrupación, conmutación y failover.

Líneas de comando para la instalación de rabbitmq en sistema operativo basado en Debian (Ubuntu, Mint) 

sudo apt-get update
sudo apt-get upgrade
sudo apt-get install erlang 
sudo apt-get install rabbitmq-server 
sudo systemctl start rabbitmq-server 
sudo rabbitmq-plugins enable rabbitmq_management 
sudo rabbitmqctl add_user admin admin
sudo rabbitmqctl set_user_tags admin administrador 
sudo rabbitmqctl set_permissions -p / admin “.*” “.*” “.*” 

Abrir el navegador y entrar a localhost:15672 y entrar con usuario: guest y contraseña: guest 

Librerías de rabbitmq 
RabbitMQ habla AMOP 0.9.1 que es un protocolo abierto, de propósito general para mensajería. Hay un número de clientes para RabbitMQ en muchos idiomas diferentes. Pika es el cliente Python recomendado por el equipo RabbitMQ

La versión de python usada para el proyecto es 2.7.
La librería de Pika para python2.7 se la instala desde ubuntu con la siguiente línea de comando: 
sudo apt-get update
sudo apt-get install python-pika



Uso del sistema:

Ejecución de cliente en python:
Abrir una consola en el directorio donde se encuentra el archivo “jobPythonClient.py” y ejecutar el comando “python jobPythonClient.py”


Ejecución de cliente en Java:
Abrir una consola en el directorio Proyecto/comunicacionJava/src/ donde se encuentra el archivo “jobJavaClient.java” y ejecutar los comandos: 

javac -cp amqp-client-4.0.2.jar jobJavaClient.java  

java -cp .:amqp-client-4.0.2.jar:slf4j-api-1.7.21.jar:slf4j-simple-1.7.22.jar jobJavaClient                                                                                         

Asegurarse de tener todos los .jar necesarios en el mismo directorio que el archivo jobJavaClient (Estos son: amqp-client-4.0.2.jar, rabbitmq-client.jar, slf4j-api-1.7.21.jar, slf4j-simple-1.7.22.jar)

Ejecución de worker en python:
Abrir una consola en el directorio donde se encuentra el archivo “worker.py”  y ejecutar el comando “python worker.py”
