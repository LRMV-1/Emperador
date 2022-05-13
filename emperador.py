# -*- coding: utf-8 -*-

from lib2to3.pytree import Node
from pickletools import read_uint1
from queue import Empty
from queue import Queue
import string


class nodo :
    def __init__(self, jugada):
        self.jugada = jugada
        self.hijos = []
    def __repr__(self):
        return str (self.jugada) + "-> []"
    
class Jugada:
    def __init__(self, carta1, carta2, puntaje):
        self.carta1 = carta1
        self.carta2 = carta2
        self.puntaje = self.determinar_puntaje (self.carta1, self.carta2) + puntaje

    def __repr__(self):
        return str(self.carta1) + " vs " + str(self.carta2) + " = " +str(self.puntaje)

    def determinar_puntaje (self, carta1, carta2):
        if (carta1 == "C" and carta2 == "C"):
            return 0
        if (carta1 == "C" and carta2 == "R"):
            return -1
        if (carta1 == "C" and carta2 == "E"):
            return 1
        if (carta1 == "R" and carta2 == "R"):
            return 0
        if (carta1 == "R" and carta2 == "E"):
            return -1
        if (carta1 == "R" and carta2 == "C"):
            return 1
        if (carta1 == "E" and carta2 == "E"):
            return 0
        if (carta1 == "E" and carta2 == "C"):
            return -1
        if (carta1 == "E" and carta2 == "R"):
            return 1

def modifica_lista (elem , lista):
    copia = lista.copy()
    copia.remove(elem)
    return copia

def make_nodo (cosa1, cosa2,puntaje):
    new_jugada = Jugada(cosa1, cosa2, puntaje)
    new_nodo = nodo(new_jugada)
    return new_nodo

def make_sons (list1, list2,puntaje):
    copia1 = list1.copy()
    end = []
    while(len(copia1)!= 0):
        copia2 = list2.copy()
        elem = copia1.pop(0)
        while (len(copia2)!=0):
            elem2 = copia2.pop(0)
            end.append(make_nodo(elem,elem2, puntaje))
    return end
        
def make_tree (list1, list2):

    #creamos la raiz y la primera gen de hijos
    root = nodo(None)
    root.hijos = make_sons(list1, list2,0)
    #print (root.hijos)
    #print(len(root.hijos))
    
    
    for i in root.hijos:
        copia1 = modifica_lista (i.jugada.carta1, list1)
        copia2 = modifica_lista(i.jugada. carta2, list2)
        i.hijos = make_sons(copia1, copia2,i.jugada.puntaje)
        
        
        for j in i.hijos:
            copia3 = modifica_lista(j.jugada.carta1, copia1)
            copia4 = modifica_lista(j.jugada.carta2, copia2)
            j.hijos = make_sons(copia3, copia4, j.jugada.puntaje)
            
            
            for k in j.hijos:
                copia5 = modifica_lista(k.jugada.carta1, copia3)
                copia6 = modifica_lista(k.jugada.carta2, copia4)
                k.hijos = make_sons(copia5, copia6, k.jugada.puntaje)
                
                
                for l in k.hijos:
                    copia7 = modifica_lista(l.jugada.carta1, copia5)
                    copia8 = modifica_lista(l.jugada.carta2, copia6)
                    l.hijos = make_sons(copia7, copia8, l.jugada.puntaje)
                    
                
    
    return root

# recorrido es una lista vacia se supone...
def DFS (origen, recorrido):

    #print(origen)
    recorrido.append (origen)
    
    if (origen.jugada != None and origen.jugada.puntaje == 3):
        return 1
    else:
        
        for i in origen.hijos:
            if DFS (i, recorrido) != 1:
                recorrido.pop()
            else:
                return 1  
        return 0
            
            
def BFS(origen, recorrido,visited):
    cola=Queue()
    visited.append(origen)
    cola.put(origen)
    i=0
    

    while(cola.qsize()>0):

        new_node=cola.get()
        
        recorrido.append(new_node)
        if(new_node.jugada!=None and new_node.jugada.puntaje==3):
            break
        i=i+1
        for neighbour in new_node.hijos:
            if neighbour not in visited:
                visited.append(neighbour)
                cola.put(neighbour)
    return 0

def main ():
    listaCartas1 = ["C", "R", "E", "C"]
    listaCartas2 = ["C", "R", "E", "C"]
    
    nodito = make_tree(listaCartas1, listaCartas2)
    
    #print(nodito)
    
    ruta = []
    resultado = DFS (nodito, ruta)
    print("La ruta DFS es:")
    print(ruta)
    print("\n")

    ruta = []
    visitados = []
    resultado2 = BFS(nodito,ruta,visitados)
    print("La ruta BFS es:")
    print(ruta)
    print(len(ruta))
    


if __name__ == '__main__':
    main ()