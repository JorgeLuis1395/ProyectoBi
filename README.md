# ProyectoBi
DISEÑO E IMPLEMENTACIÓN DE UN SISTEMA CLASIFICADOS DE SENTIMIENTOS PARA POLITICA

Integrantes:


Jorge Luis Carrillo


Roberto Toapanta

DESCRIPCIÓN:

Durante el proyecto se trabajó con las herramientas CouchDB, ElasticSearch, Logstash, Kibana y Pycharm.

CouchDB se utilizó para almacenar y filtrar los tweets.

Pycharm es un IDE que soporta lenguajes XML, HTML, XHTML y Python. Este último se utilizó para escribir los scripts que automatizaron la limpieza y el análisis de los tweets.

Logstash: Es un pipeline de procesamiento de datos que recoge los mismos de múltiples fuentes.

Elasticsearch: Permite hacer busqueda sobre texto y realizar análisis de sentimientos.

Kibana: Permite visualizar los datos de Elasticsearch. Presenta la información usando gráficos de barras, líneas, mapas o pasteles.

River: Plugin para ElasticSearch que permite indexar los documentos de couchdb para poder visualizarlos en ElasticSearch.

INSTRUCCIONES DE INSTALACIÓN 


REQUISITOS PREVIOS PARA EL FUNCIONAMIENTO DEL PROYECTO


INSTALACION COUCHDB

Para la instalación de CouchDB procedemos a escribir los siguientes comandos:


Actualizamos Ubuntu mediante el siguiente comando.


sudo apt-get update


Instalamos nuestra base de datos No SQL


sudo apt-get install couchdb –y


Verificamos la instalación de nuestra base de datos mediante la siguiente dirección:



localhost:5984/_utils




Instalación de ElasticSearch

https://www.digitalocean.com/community/tutorials/how-to-install-elasticsearch-logstash-and-kibana-elk-stack-on-ubuntu-16-04


Adquisición de Datos 


Para poder realizar  el análisis de tweets necesitamos adquirir de datos para esto se procede a ejecutar el script harvester_uio.py.



•	En el script se necesita ingresar las credenciales del API de Twitter que se puede obtener en la siguiente dirección web: https://dev.twitter.com/ 


 
•	Creamos una aplicación de twitter y dentro de estas tendremos las credenciales necesarias para poder correr el siguiente script.



•	Seleccionamos las coordenadas de la zona a cosechar los tweets del siguiente link .

•	Conectamos a la base de CouchDB donde se almacenarán los tweets recolectados en la zona de Quito.

Ejecutamos el Archivo ExtraerBaseDeDatos.py


Fase de Análisis
En esta etapa se realiza el análisis y la clasificación de los textos determinando los sentimientos del texto para esto es necesario definir el train el cual se va a definir el Sustantivo, adjetivo, verbo, emoticones y la calificación de la oración  para entrenar a nuestro clasificador de palabras.
Se ingresara el train de forma manual con 100 tweets que serán elaborados teniendo en cuenta el sustantivo, adjetivo, verbo, para generar un nuevo archivo. Este nuevo archivo servirá para el ingreso de un nuevo ingreso para nuestro train y así obtener una clasificación mayor al 80%.
El test que nos permitirá evaluar nuestro clasificador será ingresado mediante un archivo.
El clasificador utilizara un script de Python el cual se utiliza funciones como TextBlob y se clasificara mediante el algoritmo de Bayes.

Presentación de Datos
En esta fase de presentación de los datos se necesita la conexión con ElasticSearch para poder extraer nuestros datos que se encuentran presentes en la base CouchBD para esto necesitamos tener instalado el Plugin _river, head, kopf, estos plugin nos servirán para poder analizar los datos. 
Después de haber extraído los tweets e instalar Kibana se procede a realizar el análisis de los datos de forma visual mediante en mapping que tendrá la hora y la ciudad del tweet.


Análisis de Resultados


•	Podemos analizar que las personas en la ciudad de Quito envían una mayor cantidad de tweets dentro de las 16h00 y 20h00 de lo cual puede ser por el estado de ánimo del trabajo o del día que paso. Esto puede ser interesante para realizar el estudio de mercado y ofertar cierta cantidad de productos.

•	Como se puede observar el para una clasificación correcta de los sentimientos efectuados por las personas es necesario entrenar a nuestro clasificador de la mejor manera posible para poder obtener una mayor precisión.



•	En la cosecha de tweet se pudo observar que entraron tweets de los países aledaños con diferentes idiomas, esto es por las coordenas establecidas al momento de ejecutar nuestro script. Para solucionar este problema se desarrolló una vista para recoger los datos que estén solo en español y sean 
