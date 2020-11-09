
t=6
#t=8
#t=800
n=8
#n=6
#n=12
lista = [6,4,3,3,3,2,2,2]
#lista = [8,6,4,4,2,2]
#lista = [100,100,100,100,100,100,50,50,50,50,50,50]
lista_aux = []
lista_soluciones = []
suma = 0


def sumaRecursiva(t,n,lista, lista_aux, suma):
    lista_aux = lista_aux[:] #hacemos una copia de la lista_aux, ya que las listas son mutables y se pasa la referencia 
    if suma == t:
        lista_aux2 = lista_aux
        lista_soluciones.append(lista_aux2) #agregamos la solucion a la lista de soluciones 
        return
    else:
        for pos in range(n):
            lista_aux.append(lista[pos])#agregamos el elemento en la lista auxiliar
            suma = sum(lista_aux) # generamos la suma acumulativa de la lista auxiliar
            if suma == t or suma < t:
                sumaRecursiva(t,len(lista[pos+1:]),lista[pos+1:],lista_aux,suma)
                lista_aux.pop() #eliminamos el último elemento para seguir iterando
            else:
                lista_aux.pop()
        return

sumaRecursiva(t,n,lista, lista_aux, suma)

#funcion que elimina los elementos repetidos de la lista de soluciones
def elementosRepetidos(lista):
    listaAux = []
    for elemento in lista:
        if elemento not in listaAux:
            listaAux.append(elemento)
    return listaAux

#función que imprimira la salida correspondiente
def imprimirResultado(listaResultado, t):
    print (f"Suma de {t}:")
    if len(listaResultado) == 0:
        print("NADA")
    else:
        for Lista in listaResultado:
            if len(Lista) == 1:
                print(Lista[0])
            else:
                ultimo = len(Lista) - 1
                for index,elemento in enumerate(Lista):
                    if index == ultimo:
                        print(elemento)
                    else:
                        print(elemento, end="")
                        print("+", end="")

    return 




listaFinal = elementosRepetidos(lista_soluciones)
imprimirResultado(listaFinal,t)


