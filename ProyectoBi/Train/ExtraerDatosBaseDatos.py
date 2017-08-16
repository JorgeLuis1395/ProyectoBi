
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

with open('trainAdjetivos.json','r') as fp:
   cl = NaiveBayesClassifier(fp, format="json")

#Expresiones regulares de URLs
url = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
url2= '(www\.)(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
#Filtrar los tweets por # y @ por URLs
expresionRegularFiltrar = re.compile('#|@|'+url+'|'+url2)

#sys.stdout=open("Train1.json","w")
if len(db.view(view)) > 0:
    for data in db.view(view):
        json_data = {}
        json_data1 = {}
        json_data = db.get(data['id'])
        textoIngesado = data['value']
        textoIngesado1 =TextBlob(expresionRegularFiltrar.sub('', textoIngesado))
        polarity_value = textoIngesado1.sentiment.polarity * 100.0
        if polarity_value == 0:
           polarity = 'neu'
        elif polarity_value < 0:
           polarity = 'neg'
        else:
           polarity = 'pos'
        subjectivity = textoIngesado1.sentiment.subjectivity
        #json_data['label'] = {'polarity': polarity, 'polarity_value': polarity_value, 'subjectivity': subjectivity}
        print('polarity '+str(polarity)+ ' polarity_value '+str(polarity_value)+' subjectivity '+str(subjectivity))
        #try:
         #   db.save(json_data)
          #  print("guardand")
        #except:
         #   print("Error al guardar")


test=[
     ("Lo mejor del futuro es que viene un dia a la vez.", 'pos'),
     ("hijos de la chingada", 'neg'),
     ("La amistad entre dos mujeres comienza o acaba por ser un complot contra una tercera...", 'neu'),
     ("Canta las canciones", 'pos'),
     ("Un saludo para todos esos Narnianos!!!", 'pos'),
     ("MALDITOS HDP!", 'neg'),
     ("Preocupate si te deja en visto", 'neg'),
     ("Pobres personas", 'neg'),
     ("Alcoholismo es una palabra muy fuerte", 'neg'),
     ("Esto es genial", 'pos'),
     ("Ojala que te vaya bien", 'pos'),
     ("Eres un antipatico", 'pos'),
     ("Eres pesimo para esto", 'neg'),
     ("No se si hacer esto o lo otro", 'neu'),
     ("No puedo con esto", 'neg'),
     ("Creer en ti", 'pos'),
     ("No sale el proyecto", 'neg'),
     ("Que rico que sabe", 'pos'),
     ("No todo esta mal", 'neu'),
     ("Solo es peso muerto", 'neg'),
     ("Lo hiciste bien", 'pos'),
     ("Hay que ser positivo", 'pos'),
     ("No esta bien que lo hayas hecho", 'neg'),
     ("Deberia ser de otra forma", 'neu'),
     ("Los proyectos no deberian ser tan largos", 'neu'),
     ("Me regalaron un punto para pasar", 'pos'),
     ("Ya lo hizo", 'neu'),
     ("Fue un accidente", 'neg'),
     ("El examen estaba facil", 'pos'),
     ("El examen estaba imposible", 'pos'),
     ("Lo bueno si dura", 'pos'),
     ("Todo en exceso es malo", 'neg'),
     ("Te lo advierto", 'neg'),
     ("Ingeniera colabore", 'neu'),
     ("Le dieron like", 'pos'),
     ("Mi avatar es genial", 'pos'),
     ("Todos te odian", 'neg'),
     ("Hay que hacerlo", 'neu'),
     ("Quien habla mal de mi a mis espaldas mi culo lo contempla", 'neu'),
     ("El inspira confianza", 'pos'),
     ("El racismo es malo", 'neg'),
     ("En la vida es mas importante saber aceptar una derrota que celebrar una victoria", 'neu'),
     ("Que bueno que ya se acaba el semestre", 'pos'),
     ("Ya no le voy a ver", 'neg'),
     ("Un pasado no superado", 'neg'),
     ("El amor es ciego hasta que te casas", 'neu'),
     ("No hace falta un ramo de rosas para hacer sonreir a una mujer", 'neu'),
     ("A la verga con esto jajaja", 'neu'),
     ("Es genial jaja", 'pos'),
     ("Vamos con todo", 'pos'),
     ("Al fin me gradue", 'pos'),
     ("Que bueno que no les vuelvo a ver", 'neu'),
     ("Las putas son putas", 'neg'),
    ("Esto no esta bien", 'neg')
 ]

#cl.accuracy(test, format=None)
#sys.stdout.close()
print(cl.accuracy(test))

