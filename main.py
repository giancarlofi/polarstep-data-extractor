 
# Python program to read polarsteps exported files
import os
import json
import sys
from htmldoc import HtmlDoc

"""
n = len(sys.argv)
print("Total arguments passed:", n)
 
# Arguments passed
print("\nName of Python script:", sys.argv[0])
 
print("\nArguments passed:", end = " ")
for i in range(1, n):
    print(sys.argv[i], end = " ")
"""
print ("DON'T FORGET: CHANGE THE SOURCE FILE VARS [infoPathFile,dirData,htmlFileName,tripName] ")
# Percorso del file che contiene le informazioni
infoPathFile = 'corsica-del-sud/trip.json'
f = open(infoPathFile)
data = json.load(f)
f.close()

# Predisposizione creazione html
# 1 parametro: cartella dove si trovano i dati del viaggio
# 2 parametro: nome del file html risultante, verrà messo nella cartella 1 parametro
# 3 parametro: title del file html
dirData = "corsica-del-sud"
htmlFileName = "corsica-del-sud.html"
tripName = "Corsica del sud 2024"
html = HtmlDoc(dirData,htmlFileName,tripName)

for i in data['all_steps']:
    	html.addTable(i)





  
