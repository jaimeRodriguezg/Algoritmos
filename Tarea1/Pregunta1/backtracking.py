lista_aux = []
lista_soluciones = []
suma = 0
listaNueva= []
    
#funcion que verifica los resultados de la sumarecursiva usando backtracking
def sumaRecursiva(t,n,lista, lista_aux, suma):
    lista = lista [:]
    lista_aux = lista_aux[:] #hacemos una copia de la lista_aux, ya que las listas son mutables y se pasa la referencia 
    if suma == t:
        lista_soluciones.append(lista_aux) #agregamos la solucion a la lista de soluciones 
        return
    else:
        for pos in range(n):
            lista_aux.append(lista[pos])#agregamos el elemento en la lista auxiliar
            suma = sum(lista_aux) # generamos la suma acumulativa de la lista auxiliar
            if suma == t or suma < t:
                sumaRecursiva(t,len(lista[pos+1:]),lista[pos+1:],lista_aux,suma)
            lista_aux.pop()#eliminamos el último elemento para seguir iterando
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


archivo = open("data.txt", 'r')
lineas = archivo.readlines()
print (lineas) 

for linea in lineas:
    lista = []
    print(f"la linea es {linea}")
    string= ""
    for index,elemento in enumerate(linea):
        if elemento == " ":
            listaNueva.append(string)
            string = ""
        else:
            string += elemento
            if index == len(linea) - 2:
                listaNueva.append(string)
    for index, elemento in enumerate(listaNueva):
        if elemento != " " and elemento != "\n":
            lista.append(int(elemento))
    listaNueva = []
    t = lista[0]
    n = lista[1]
    lista = lista[2:]
    sumaRecursiva(t,n,lista, lista_aux, suma)
    listaFinal = elementosRepetidos(lista_soluciones)
    lista_soluciones = []
    imprimirResultado(listaFinal,t)
    listaFinal = []