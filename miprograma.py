from lxml import etree
from urllib.request import urlopen
import tkinter as tk
from tkinter import simpledialog
import sys
import funcion

fs = open(sys.argv[1],"w")
application_window = tk.Tk()

pagina = simpledialog.askstring("Input", "Escribe un link xml: ",
                                parent=application_window)
ns={"Atom" : "http://www.w3.org/2005/Atom"}
parser=etree.XMLParser()
tree=etree.parse(urlopen(pagina),parser)
for node in tree.xpath('//Atom:entry/Atom:title', namespaces=ns) :
   print (node.text)
   fs.write(node.text + "\n")
fs.close()

entry = simpledialog.askstring("Input", "Escribe el nombre del fichero donde se han guardado las entradas: ",
                                parent=application_window)

listaPalabras = list()

fh = open(entry,"r")
line = fh.readline()
while line:
  words = line.split()
  for w in words:
    listaPalabras.append(w)
  line = fh.readline()
fh.close()
print(listaPalabras)


undict = funcion.contador(listaPalabras)

print("""
Este es el contador de las palabras totales que aparecen en los titulos
de las imagenes del xml introducido:
	""")

for K in undict.keys():
	print(K + " ----> " + str(undict[K]))

