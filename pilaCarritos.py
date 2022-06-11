class nodo:
    def __init__(self, num):
        self.num = num
        self.siguiente = None
        self.anterior = None

class pila():
    def __init__(self):
        self.primero=None
        self.ultimo=None

    def agregar(self,num):
        nuevo=nodo(num)

        if (self.primero==None):
            self.primero=nuevo
        else:
            nuevo.anterior=self.ultimo
            self.ultimo.siguiente=nuevo
        self.ultimo=nuevo

    def imprimir(self):
        aux = self.primero
        while (aux != None):
            print(aux.num)
            aux = aux.siguiente

    def cant(self):
        x=0
        aux = self.primero
        while (aux != None):
            x+=1
            aux = aux.siguiente

        return x

    def pop(self):
        aux = self.ultimo
        x=self.ultimo.num
        if (aux.anterior != None):
            self.ultimo = aux.anterior
            aux.anterior.siguiente = None
        else:
            self.primero = None
            self.ultimo = None
        del aux
        return x