class nodo:
    def __init__(self, idPersona, numCarrito):
        self.idPersona = idPersona
        self.numCarrito = numCarrito
        self.siguiente = None
        self.anterior = None


class cola():
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def agregar(self, idPersona, numCarrito):
        nuevo = nodo(idPersona, numCarrito)
        if (self.primero == None):
            self.primero = nuevo
        else:
            nuevo.anterior = self.ultimo
            self.ultimo.siguiente = nuevo
        self.ultimo = nuevo

    def imprimir(self):
        aux = self.primero
        c = 1
        while (aux != None):
            print(str(c) + ") Id Cliente:", aux.idPersona, "  Numero de carrito:", aux.numCarrito)
            c += 1
            aux = aux.siguiente

    def pop(self):
        aux = self.primero
        if (aux.siguiente != None):
            self.primero = aux.siguiente
            aux.siguiente.anterior = None
        else:
            self.primero = None
            self.ultimo = None
        del aux

    def borrar(self):
        aux = self.primero
        while (aux != None):
            if (aux.siguiente != None):
                nodoBorrar = aux
                self.primero = aux.siguiente
                del nodoBorrar
                return aux.numCarrito
            else:  # Eliminar un elemento de una lista de un solo elemento
                self.primero = None
                self.ultimo = None
                nodoBorrar = aux
                del nodoBorrar
                return aux.numCarrito

        aux = aux.siguiente

    def cant(self):
        x=0
        aux = self.primero
        while (aux != None):
            x+=1
            aux = aux.siguiente

        return x