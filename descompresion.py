from zipfile import ZipFile

with ZipFile('com.zip') as myzip:
  myzip.extractall()