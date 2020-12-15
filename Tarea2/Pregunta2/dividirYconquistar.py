

def sum_max_dif_aux(n, subLista): # sub lista siempre tendra al menos 2 elementos
    listaListasMinMax = []

    if subLista[0] < subLista[1]: # se comparan los dos primeros valores
        listaListasMinMax.append([subLista[0], subLista[1]]) # lista inicial (minimo, maximo)
    else:
        listaListasMinMax.append([subLista[1], subLista[0]]) # lista inicial (minimo, maximo)

    for j in range(n-2): # itera para buscar el maximo y minimo para los subArreglos restantes
        val_siguiente = subLista[j+2]
        #j1 = j+1
        if listaListasMinMax[-1][0] > val_siguiente:
            listaListasMinMax.append([val_siguiente, listaListasMinMax[j][1]]) 
        elif listaListasMinMax[-1][1] < val_siguiente:
            listaListasMinMax.append([listaListasMinMax[j][0], val_siguiente]) 
        else:
            listaListasMinMax.append([listaListasMinMax[j][0], listaListasMinMax[j][1]]) 
    return listaListasMinMax


def sum_max_dif(n, lista):
    listaListasMinMax = []
    valReturn = 0
    if n > 1:
        for i in range(n - 1): # itera entre el primer valor y el penultimo
            subArreglo = lista[i:n]
            print("SubArreglo:")
            print(subArreglo)
            n_sub = n-i
            #print(n_sub)
            print("Resultados SubArreglo:")
            lista_min_max_aux = sum_max_dif_aux(n_sub, subArreglo)
            print(lista_min_max_aux)
            for j in range(len(lista_min_max_aux)):
                valReturn += lista_min_max_aux[j][1]
                valReturn -= lista_min_max_aux[j][0]

            
            print("Fin SubArreglo\n")
    return valReturn
        
            
        

def main():
    arrLen = input("Ingresa Largo de Arreglo: \n>>> ")
    strLista = input("Ingresa Lista ( Ej: >>> 0 1 9 2 ): \n>>> ")
    listaValores = strLista.split(" ")
    listaValores = list(map(int, listaValores)) 
    pa = sum_max_dif(int(arrLen), listaValores)
    print("Resultado:")
    print(pa)


if __name__ == "__main__":
    main()