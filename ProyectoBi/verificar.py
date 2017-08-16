from textblob import TextBlob


def leerArchivo():
    archi = open('dic_adj.txt', 'r')
    lineas = archi.read()
    archi.close()
    return lineas


# Funcion para conteo
def listaPalabrasAFrecDict(listaPalabrasP):
    palabraFrec = [listaPalabrasP.count(p) for p in listaPalabrasP]
    return dict(zip(listaPalabrasP, palabraFrec))


# Funcion de ordenamiento
def ordenarFreqDict(freqdict):
    aux = [(key) for key in freqdict]
    aux.sort()
    aux.reverse()
    return aux


# Funcion para conteo
i = 0
j = 0
v = 0
k = 0
dic_adj = open("dic_adj.txt", "w")
# dic_verb = open("dic_ver.txt","w")

# Funcion para Generar Diccionario de JJ
diccionario_adj = list()
diccionario_verb = list()

with open('tweets.txt') as fp:
    for line in fp:
        blob = TextBlob(line)
        for word, pos in blob.tags:
            if pos == 'NN':
                i = i + 1
            if pos == 'JJ':
                j = j + 1
                diccionario_adj.append(str(word))
            if pos == 'VB':
                v = v + 1
                diccionario_verb.append(str(word))
        i = 0
        j = 0
        v = 0
for s in diccionario_adj:dic_adj.write(str(s) + '\n')
# for v in diccionario_verb:dic_verb.write(str(v) + '\n')
dic_adj.close()
# dic_verb.close()

# Funcion para contar una sola palabra y generar diccionario

texto = leerArchivo()
listaPalabras = texto.split()
# diccionario = list(set(listaPalabras))
# 4. Convertir lista en diccionario
diccionario = listaPalabrasAFrecDict(listaPalabras)
# 5. Ordenar diccionario
diccionarioOrdenado = ordenarFreqDict(diccionario)

archi = open('dic_adjfinal.txt', 'w')

for s in diccionarioOrdenado:
    blob = TextBlob(s)
    archi.write(str(blob).replace('\n', '') + "\": " + str(blob.sentiment.polarity) + ", \"")
archi.close()