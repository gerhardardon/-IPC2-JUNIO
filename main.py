from pilaCarritos import*
from listaPersonas import*
from colaCaja import*

class bcolor:
    morado = "\033[1;35m"
    reset = '\033[0m'

lstCarritos=pila()
lstPersona=lista()
lstCaja=cola()

def menu():
    global lstCarritos, lstPersona, lstCaja
    print(bcolor.morado+"\n\n\n==========MENU=========="+bcolor.reset)
    print("Seleccione una opción...\n1)   Ingreso de datos\n2)   Nuevo cliente\n3)   Ver cliente\n4)   Caja registradora\n5)   Visualizar datos\n6)   Salir")
    x=input()
    if x == "1":
        lstCarritos=pila()
        print(bcolor.morado+"Cuantos carritos desea?"+bcolor.reset)
        cant=input()
        if int(cant)<=0:
            print(bcolor.morado+"INGRESE UN NÚMERO VALIDO"+bcolor.reset)
            menu()
        i=1
        while (i <= int(cant)):
            lstCarritos.agregar(i)
            i += 1
        menu()
    elif x=="2":
        i=1
        if(i<=lstCarritos.cant()):
            print(bcolor.morado+"Ingrese ID"+bcolor.reset)
            identificacion=input()
            print(bcolor.morado+"Ingrese nombre:"+bcolor.reset)
            name=input()
            lstPersona.agregar(identificacion,name,lstCarritos.pop())
            print(bcolor.morado+"CLIENTE CREADO CON EXITO!"+bcolor.reset)
        else:
            print(bcolor.morado+"Ya no quedan carritos disponibles :/"+bcolor.reset)
        menu()
    elif x=="3":
        print(bcolor.morado+"Listado de clientes:"+bcolor.reset)
        lstPersona.imprimir()
        print(bcolor.morado + "Ingrese una opción..." + bcolor.reset+"\n1)   Pagar\n2)   Regresar")
        x=input()
        if x=="1":
            print(bcolor.morado+"Ingrese el ID del cliente:"+bcolor.reset)
            x=input()
            if lstPersona.buscarId(x)==True:
                lstCaja.agregar(x,lstPersona.buscarCarrito(x))
                print(bcolor.morado+"CLIENTE ENVIADO A LA COLA CON EXITO!"+bcolor.reset)
                lstPersona.borrar(x)
                menu()
            else:
                print(bcolor.morado+"EL ID NO EXISTE :/"+bcolor.reset)
        elif x=="2":
            menu()
        else:
            print("Ingrese un número valido :/")
        menu()
    elif x=="4":
        if lstCaja.cant()==0:
            print(bcolor.morado+"NO HAY CLIENTES EN LA CAJA"+bcolor.reset)
            menu()
        lstCaja.imprimir()
        print(bcolor.morado+"Desea que avance la cola (si/no)?"+bcolor.reset)
        x=input()
        if x=="si":
            lstCarritos.agregar(lstCaja.borrar())
            print(bcolor.morado+"LISTO, EL CLIENTE PAGO Y REGRESO EL CARRITO!"+bcolor.reset)

        elif x=="no":
            menu()
        else:
            print(bcolor.morado+"INGRESE UNA OPCION VALIDA :/"+bcolor.reset)
        menu()
    elif x=="5":
        print("LISTA CARRITOS:")
        lstCarritos.imprimir()
        print("\nLISTA PERSONAS:")
        lstPersona.imprimir()
        print("\nLISTA CAJA:")
        lstCaja.imprimir()
        menu()
    elif x=="6":
        print(bcolor.morado+"BYE BYE ;)"+bcolor.reset)
        exit()
    else:
        print(bcolor.morado+"Seleccione una opción válida :/"+bcolor.reset)
        menu()

menu()