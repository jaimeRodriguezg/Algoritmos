import math


puntos = [1,2,4,8,9]



def mergeSort(arr) :
    if (len(arr) == 1):
        return arr

    if (len(arr) > 1):
        middle =  math.ceil(len(arr)/2)
        print(f'middle es {middle}')
        left = arr[0:middle]
        print(f'left es {left}')
        right = arr [middle:len(arr)]
        print(f'right es {right}')

        left = mergeSort(left)
        right = mergeSort(right)

        result = merge(left,right)

        return result

def merge(left,right):
    global MaximaDiferencia
    MaximaDiferencia = 0
    result = []
    while(len(left) > 0 and len(right) > 0):
        print(f'left es --------------{left}')
        print(f'right es ------------- {right}')
        if (left[0] <= right[0]):
            aux = left.pop(0)
            result.append(aux)
        else:
            aux = right.pop(0)
            result.append(aux)
        
    print(f'result es ------------{result}')
    
    while(len(left) > 0):
        aux = left.pop(0)
        result.append(aux)

    while(len(right) > 0):
        aux = right.pop(0)
        result.append(aux)

    diferencia = 0
    print(f'result es {result}')
    if (len(result) > 1) :
        diferencia = result[1] - result[0]
    else:
        diferencia = result[0]
    
    print(f'diferencia es {diferencia}')
    if (MaximaDiferencia >=0) :
        print("entre")
        if(diferencia > MaximaDiferencia):
            MaximaDiferencia = diferencia
    
    print(f"MaximaDiferencia es {MaximaDiferencia}")

    return result

mergeSort(puntos)

print(f'el maximo es {MaximaDiferencia}')
    



