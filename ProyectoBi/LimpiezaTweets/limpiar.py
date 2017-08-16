
import couchdb
import sys
import textblob
import os
import re
import json

from couchdb import view
from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier
import urllib3
import textblob
from couchdb import view
from textblob import TextBlob

URL = 'localhost'
db_name = 'bireplica'
server = couchdb.Server('http://'+URL+':5984/')

try:
    print(db_name)
    db = server[db_name]
    print('conexion exitosa')
except:
    sys.stderr.write("Error: Base de datos no encontrado. Terminar\n")
    sys.exit()


view = "vistaproyecto/vistaproyecto"

with open('train.json','r') as fp:
   cl = NaiveBayesClassifier(fp, format="json")

#Expresiones regulares de URLs
url = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
url2= '(www\.)(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
#Filtrar los tweets por # y @ por URLs
expresionRegularFiltrar = re.compile('#|@|'+url+'|'+url2)

sys.stdout=open("tweets.txt","w")
if len(db.view(view)) > 0:
    for data in db.view(view):
        json_data = {}
        json_data = db.get(data['id'])
        textoIngesado = data['value']
        textoIngesado =TextBlob(expresionRegularFiltrar.sub('', textoIngesado))
        #textoIngesado1=textoIngesado.translate(to="en")
        print(textoIngesado)
sys.stdout.close()