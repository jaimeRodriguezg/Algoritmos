import time


# sub lista siempre tendra al menos 2 elementos
def sum_max_dif_aux(n, subLista): 
    total = 0
    maximo = 0
    minimo = 0

    # se comparan los dos primeros valores
    if subLista[0] < subLista[1]: 
        maximo = subLista[1]
        minimo = subLista[0]
    else:
        maximo = subLista[0]
        minimo = subLista[1]

    total += maximo
    total -= minimo

    # itera para buscar el maximo y minimo para los subArreglos restantes
    for j in range(n-2): 
        val_siguiente = subLista[j+2]
        #j1 = j+1
        if minimo > val_siguiente:            
            minimo = val_siguiente
        elif maximo < val_siguiente:
            maximo = val_siguiente
        else:
            pass
        total += maximo
        total -= minimo

    return total


def sum_max_dif(n, lista):
    valReturn = 0
    if n > 1:
        # itera entre el primer valor y el penultimo
        for i in range(n - 1): 
            subArreglo = lista[i:n]
            n_sub = n-i
            # obtiene resultados de sub arreglo
            valReturn += sum_max_dif_aux(n_sub, subArreglo)
            # Fin Sub Arreglo
    return valReturn
        
            
        

def main():
    arrLen = input("").strip()
    strLista = input("").strip()
    listaValores = strLista.split(" ")
    listaValores = list(map(int, listaValores)) 
    resultado = sum_max_dif(int(arrLen), listaValores)
    print(resultado)


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- {} seconds ---".format(time.time() - start_time))