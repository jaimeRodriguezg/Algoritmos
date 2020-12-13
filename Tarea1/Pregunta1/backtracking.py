lista_aux = []
lista_soluciones = []
suma = 0
listaNueva= []
    
# Función que verifica los resultados de la suma usando backtracking.
# Genera una listas de las soluciones --> [[6], [4,2], [3,3], [2,2,2]].
def sumaRecursiva(t,n,lista, lista_aux, suma):
    lista_aux = lista_aux[:] #hacemos una copia de la lista_aux, ya que las listas son mutables y se pasa la referencia 
    if suma == t:
        lista_soluciones.append(lista_aux) #agregamos la solución a la lista de soluciones 
        return
    else:
        for pos in range(n):
            lista_aux.append(lista[pos]) #agregamos el elemento en la lista auxiliar
            suma = sum(lista_aux) #generamos la suma acumulativa de la lista auxiliar
            if suma == t or suma < t:
                sumaRecursiva(t,len(lista[pos+1:]),lista[pos+1:],lista_aux,suma) #llamamos a la función de forma recursiva con nuevos parametros, acotando la lista principal
            lista_aux.pop() #eliminamos el último elemento para seguir iterando
        return


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

#se leen inputs y se itera y se llama la funcion de sumaRecursiva que genera el backtracking
while True:
    linea = input("")
    lista = linea.split(" ")
    lista = list(map(int, lista))
    t = lista[0]
    n = lista[1]
    if t == 0 and n == 0:
        break
    else:
        lista.pop(0)
        lista.pop(0)
        sumaRecursiva(t,n,lista, lista_aux, suma)
        listaFinal = elementosRepetidos(lista_soluciones)
        lista_soluciones = []
        imprimirResultado(listaFinal,t)
        listaFinal = [] 
    