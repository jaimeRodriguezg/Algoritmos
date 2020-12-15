import time

def suma_maximos_subarreglos(arreglo,resultado):
    if(len(arreglo)==1):
        return arreglo[0]
    else:
        inicio=0
        fin=len(arreglo)-1
        pos_max=arreglo.index(max(arreglo))
        resultado = resultado + arreglo[pos_max]*(fin-pos_max+1)*(pos_max-inicio+1)
        if pos_max==inicio:
            resultado= resultado + suma_maximos_subarreglos(arreglo[pos_max+1:],0)
        elif pos_max==fin:
            resultado= resultado + suma_maximos_subarreglos(arreglo[:pos_max],0)
        else:
            resultado = resultado + suma_maximos_subarreglos(arreglo[:pos_max],0)+suma_maximos_subarreglos(arreglo[pos_max+1:],0)
        return resultado

def suma_minimos_subarreglos(arreglo,resultado):
    if(len(arreglo)==1):
        return arreglo[0]
    else:
        inicio=0
        fin=len(arreglo)-1
        pos_min=arreglo.index(min(arreglo))
        resultado = resultado + arreglo[pos_min]*(fin-pos_min+1)*(pos_min-inicio+1)
        if pos_min==inicio:
            resultado= resultado + suma_minimos_subarreglos(arreglo[pos_min+1:],0)
        elif pos_min==fin:
            resultado= resultado + suma_minimos_subarreglos(arreglo[:pos_min],0)
        else:
            resultado = resultado + suma_minimos_subarreglos(arreglo[:pos_min],0)+suma_minimos_subarreglos(arreglo[pos_min+1:],0)
        return resultado


def main():
    int(input("").strip())
    listaString=input("").strip().split()
    lista = list(map(int, listaString)) 
    resultado = suma_maximos_subarreglos(lista,0)-suma_minimos_subarreglos(lista,0)
    print(resultado)


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- {} seconds ---".format(time.time() - start_time))