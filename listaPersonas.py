class nodo:
    def __init__(self, id,nombre,carrito):
        self.id = id
        self.nombre = nombre
        self.carrito = carrito
        self.siguiente = None


class lista():
    def __init__(self):
        self.primero=None
        self.ultimo=None

    def agregar(self,id,nombre,carrito):
        nuevo=nodo(id,nombre, carrito)
        if (self.primero==None):
            self.primero=nuevo
        else:
            self.ultimo.siguiente=nuevo
        self.ultimo=nuevo

    def imprimir(self):
        aux = self.primero
        while (aux != None):
            print("ID:",aux.id,"\nNOMBRE:",aux.nombre,"\nCARRITO:",aux.carrito,"\n")
            aux = aux.siguiente

    def buscarId(self,id):
        aux = self.primero
        while (aux != None):
            if(id==aux.id):
                return True
            aux = aux.siguiente
        return False

    def buscarCarrito(self,id):
        aux = self.primero
        while (aux != None):
            if(id==aux.id):
                return aux.carrito
            aux = aux.siguiente

    def borrar(self,valorBuscado_):
        aux=self.primero
        while(aux!=None):
            if (aux.id==valorBuscado_): #eliminar el primer valor
                if(aux.siguiente!=None):
                    nodoBorrar=aux
                    self.primero=aux.siguiente
                    del nodoBorrar
                    return
                else: #Eliminar un elemento de una lista de un solo elemento
                    self.primero=None
                    self.ultimo=None
                    del aux
                    return

            if(aux.siguiente!=None):
                if (aux.siguiente.id==valorBuscado_):
                    # eliminar de la mitad de la lista
                    nodoEliminar=aux.siguiente
                    if (aux.siguiente.siguiente!=None):
                        aux.siguiente=aux.siguiente.siguiente
                        del nodoEliminar
                        return
                    else:
                        #Eliminar el ultimo
                        NodoBorrar=aux.siguiente
                        aux.siguiente=None
                        self.ultimo=aux
                        del NodoBorrar
                        return

            aux=aux.siguiente