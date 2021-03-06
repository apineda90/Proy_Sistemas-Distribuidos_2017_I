#!/usr/bin/env python
import pika
import time
import zipfile
import os

def comprimir(nombreArchivo):
    if os.path.isfile('ParaComprimir/'+nombreArchivo):
        print('Comprimiendo el archivo ' + nombreArchivo)
        jungle_zip = zipfile.ZipFile(nombreArchivo + '.zip', 'w')
        # jungle_zip.write('ParaComprimir/prueba.txt', compress_type=zipfile.ZIP_DEFLATED)
        jungle_zip.write('ParaComprimir/' + nombreArchivo, compress_type=zipfile.ZIP_DEFLATED)
        jungle_zip.close()
        print('Compresion realizada exitosamente')
    else:
        print('El archivo '+ nombreArchivo+' no existe en el directorio ')
        print('Compresion no realizada')




connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='192.168.182.139'))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)
print(' [*] Esperando mensajes. Para salir presione CTRL+C')

def callback(ch, method, properties, body):
    comprimir(body)
    time.sleep(body.count(b'.'))
    print('Fin de ejecucion..')
    print(' [*] Esperando mensajes. Para salir presione CTRL+C')
    print('                  ')
    ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback,
                      queue='task_queue')
channel.start_consuming()


