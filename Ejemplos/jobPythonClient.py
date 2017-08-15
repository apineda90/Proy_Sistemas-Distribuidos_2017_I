#!/usr/bin/env python
import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='192.168.184.221'))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)

nombre = raw_input('Introduzca el nombre(con extension) del archivo a comprimir (ejemplo: file.jpg) ')

message = ' '.join(sys.argv[1:]) or nombre
channel.basic_publish(exchange = '',
                      routing_key = 'task_queue',
                      body = message,
                      properties = pika.BasicProperties(
                         delivery_mode = 2, # make message persistent
                      ))
print("Usted envio el archivo: %r" % message)
connection.close()



