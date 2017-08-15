from zipfile import ZipFile
with ZipFile('com1.zip', 'w') as myzip:
    myzip.write('prueba.txt')
    myzip.write('prueba2.txt')
