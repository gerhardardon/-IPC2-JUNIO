import xml.etree.ElementTree as ET
from tkinter import Tk
from tkinter import filedialog as fd
import webbrowser
from os import system

arbol=None
raiz=None
empleados=""
cds=""

def buscarEmpleado():
    global arbol, raiz
    print("Ingrese el id...")
    id = input()
    for depto in raiz:
        for empleado in depto:
            if id == empleado.attrib['id']:
                print("\nID:", empleado.attrib['id'])
                print("NOMBRE:", empleado.findall('nombre')[0].text)
                print("PUESTO:", empleado.findall('puesto')[0].text)
                print("SALARIO:", empleado.findall('salario')[0].text)


def modificarEmpleado():
    global arbol, raiz,empleados
    print("\nIngrese el id...")
    id = input()
    for depto in raiz:
        for empleado in depto:
            if id == empleado.attrib['id']:
                print("\nIngrese nuevo nombre...")
                x = input()
                empleado.findall('nombre')[0].text = x

                print("Ingrese nuevo puesto...")
                x = input()
                empleado.findall('puesto')[0].text = x

                print("Ingrese nuevo salario...")
                x = input()
                empleado.findall('salario')[0].text = x
    arbol.write(empleados)
    print("\nDatos cambiados con exito!!")


def eliminarEmpleado():
    global arbol, raiz,empleados
    print("\nIngrese el id...")
    id = input()
    for depto in raiz:
        for empleado in depto:
            if id == empleado.attrib['id']:
                depto.remove(empleado)
    arbol.write(empleados)
    print("\nDatos borrados con exito!!")


def verEmpleados():
    global arbol, raiz
    for depto in raiz:
        print("\n-" + depto.attrib['departamento'])
        for empleado in depto:
            print("\t-ID:", empleado.attrib['id'])
            print("\t   -NOMBRE:", empleado.findall('nombre')[0].text)
            print("\t   -PUESTO:", empleado.findall('puesto')[0].text)
            print("\t   -SALARIO:", empleado.findall('salario')[0].text)


def buscarDisco():
    global arbol, raiz
    print("Ingrese el nombre del disco...")
    x = input()
    for cd in raiz:
        if x == cd.findall('title')[0].text:
            print("\nNOMBRE:", cd.findall('title')[0].text)
            print("ARTISTA:", cd.findall('artist')[0].text)
            print("PAIS:", cd.findall('country')[0].text)
            print("DISQUERA:", cd.findall('company')[0].text)
            print("PRECIO:", cd.findall('price')[0].text)
            print("AÑO:", cd.findall('year')[0].text)


def modificarDisco():
    global arbol, raiz,cds
    print("Ingrese el nombre del disco...")
    x = input()
    for cd in raiz:
        if x == cd.findall('title')[0].text:
            print("\nIngrese nuevo artista...")
            x = input()
            cd.findall('artist')[0].text = x

            print("Ingrese nuevo pais...")
            x = input()
            cd.findall('country')[0].text = x

            print("Ingrese nueva disquera...")
            x = input()
            cd.findall('company')[0].text = x

            print("Ingrese nuevo precio...")
            x = input()
            cd.findall('price')[0].text = x

            print("Ingrese nuevo año...")
            x = input()
            cd.findall('year')[0].text = x
    arbol.write(cds)
    print("\nDatos cambiados con exito!!")


def eliminarDisco():
    global arbol, raiz,cds
    print("Ingrese el nombre del disco...")
    x = input()
    for cd in raiz:
        if x == cd.findall('title')[0].text:
            raiz.remove(cd)
    arbol.write(cds)
    print("\nDatos eliminados con exito!!")

def verDiscos():
    global arbol, raiz
    for cd in raiz:
        print("\n-NOMBRE:", cd.findall('title')[0].text)
        print("   -ARTISTA:", cd.findall('artist')[0].text)
        print("   -PAIS:", cd.findall('country')[0].text)
        print("   -DISQUERA:", cd.findall('company')[0].text)
        print("   -PRECIO:", cd.findall('price')[0].text)
        print("   -AÑO:", cd.findall('year')[0].text)


def graficaEmpleados():
    global arbol, raiz
    x = ""
    x += "digraph G { \n"
    x += "node[shape=box] \n"
    x += "nodoRaiz[label=\"Empresa\"] \n"
    for depto in raiz:
        nodoDepto = "nodo" + depto.attrib['departamento']
        x += nodoDepto + "[label=\"" + depto.attrib['departamento'] + "\"] \n"
        x += "nodoRaiz ->" + nodoDepto + "\n"

        for empleado in depto:
            nodoEmpleado = "nodoEmpleado" + empleado.attrib['id']
            x += nodoEmpleado + "[label=\"Empleado " + empleado.attrib['id'] + " \"] \n"
            x += nodoDepto + "->" + nodoEmpleado + "\n"

            nodo1 = "nodoNombre" + empleado.attrib['id']
            x += nodo1 + "[label=\"Nombre: " + empleado.findall('nombre')[0].text + " \"] \n"
            x += nodoEmpleado + "->" + nodo1 + "\n"

            nodo2 = "nodoPuesto" + empleado.attrib['id']
            x += nodo2 + "[label=\"Puesto: " + empleado.findall('puesto')[0].text + " \"] \n"
            x += nodoEmpleado + "->" + nodo2 + "\n"

            nodo3 = "nodoSalario" + empleado.attrib['id']
            x += nodo3 + "[label=\"Salario: " + empleado.findall('salario')[0].text + " \"] \n"
            x += nodoEmpleado + "->" + nodo3 + "\n"

    x += "}"
    archivoDot = open("empleados.dot", 'w', encoding="utf-8")
    archivoDot.write(x)
    archivoDot.close()


def graficaDiscos():
    global arbol, raiz
    x = ""
    x += "digraph G { \n"
    x += "node[shape=box] \n"
    x += "nodoRaiz[label=\"Catalogo\"] \n"

    i = 0
    for cd in raiz:
        nodoDisco = "nodoDisco" + str(i)
        x += nodoDisco + "[label=\"" + "Disco" + "\"] \n"
        x += "nodoRaiz ->" + nodoDisco + "\n"
        i += 1

        nodo1 = "nodoTitulo" + str(i)
        tit = cd.findall('title')[0].text
        tit = tit.replace('"', '\\"')
        x += nodo1 + "[label=\"Titulo: " + tit + "\"] \n"
        x += nodoDisco + "->" + nodo1 + "\n"

        nodo2 = "nodoartist" + str(i)
        x += nodo2 + "[label=\"Artista: " + cd.findall('artist')[0].text + "\"] \n"
        x += nodoDisco + "->" + nodo2 + "\n"

        nodo3 = "nodocountry" + str(i)
        x += nodo3 + "[label=\"Pais: " + cd.findall('country')[0].text + "\"] \n"
        x += nodoDisco + "->" + nodo3 + "\n"

        nodo4 = "nodocompany" + str(i)
        x += nodo4 + "[label=\"Disquera: " + cd.findall('company')[0].text + "\"] \n"
        x += nodoDisco + "->" + nodo4 + "\n"

        nodo5 = "nodoprice" + str(i)
        x += nodo5 + "[label=\"Precio: " + cd.findall('price')[0].text + "\"] \n"
        x += nodoDisco + "->" + nodo5 + "\n"

        nodo6 = "nodoyear" + str(i)
        x += nodo6 + "[label=\"Año: " + cd.findall('year')[0].text + "\"] \n"
        x += nodoDisco + "->" + nodo6 + "\n"

    x += "}"
    archivoDot = open("discos.dot", 'w', encoding="utf-8")
    archivoDot.write(x)
    archivoDot.close()


def menu():
    global arbol, raiz, empleados,cds
    print("\n\n==========MENU==========")
    print("Seleccione una opción...\n1) Carga de datos\n2) Gestion de empleados\n3) Gestion de Discos\n4) Reportes\n5) Salir")
    x=input()
    if x=="1":
        print("Seleccione el XML de empleados")
        Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
        empleados = fd.askopenfilename(title="Select file")

        print("Seleccione el XML de discos")
        Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
        cds = fd.askopenfilename(title="Select file")

        menu()
    elif x=="2":
        arbol = ET.parse(empleados)
        raiz = arbol.getroot()
        print(" a) Ver empleado\n b) Modificacion\n c) Eliminacion\n d) Ver todo\n e) Generar archivo\n f) Menu")
        x = input()
        if x == "a":
            buscarEmpleado()

        elif x == "b":
            modificarEmpleado()
        elif x == "c":
            eliminarEmpleado()
        elif x == "d":
            verEmpleados()
        elif x == "e":
            graficaEmpleados()
            print("Grafica generada con exito!")
        elif x == "f":
            menu()
        menu()
    elif x=="3":
        arbol = ET.parse(cds)
        raiz = arbol.getroot()
        print(" a) Ver disco\n b) Modificacion\n c) Eliminacion\n d) Ver todo\n e) Generar archivo\n f) Menu")
        x = input()
        if x == "a":
            buscarDisco()
        elif x == "b":
            modificarDisco()
        elif x == "c":
            eliminarDisco()
        elif x == "d":
            verDiscos()
        elif x == "e":
            graficaDiscos()
            print("Grafica generada con exito!")
        elif x == "f":
            menu()
        menu()
    elif x=="4":
        print(" a) Reporte de empleados\n b) Reporte de discos\n c) Menu")
        x = input()
        if x == "a":
            try:
                system('dot -Tpng ' + "empleados" + '.dot -o ' "empleados" '.png')
                webbrowser.open_new_tab("empleados" + '.png')
            except:
                print("")
        elif x == "b":
            try:
                system('dot -Tpng ' + "discos" + '.dot -o ' "discos" '.png')
                webbrowser.open_new_tab("discos" + '.png')
            except:
                print("")
        elif x == "c":
            menu()
        menu()
    elif x=="5":
        exit()

menu()