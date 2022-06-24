import xml.etree.ElementTree as ET
from tkinter import Tk
from tkinter import filedialog as fd

def buscarDisco():
    arbol = ET.parse(cds)
    raiz = arbol.getroot()
    print("Ingrese el año de los discos...")
    x = input()
    for cd in raiz:
        if x == cd.findall('year')[0].text:
            print("\nNOMBRE:", cd.findall('title')[0].text)
            print("ARTISTA:", cd.findall('artist')[0].text)
            print("PAIS:", cd.findall('country')[0].text)
            print("DISQUERA:", cd.findall('company')[0].text)
            print("PRECIO:", cd.findall('price')[0].text)
            print("AÑO:", cd.findall('year')[0].text)

print("Seleccione el XML de discos")
Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
cds = fd.askopenfilename(title="Select file")
print("XML CARGADO CON EXITO!!!")
buscarDisco()
