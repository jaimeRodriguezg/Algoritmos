def suma_recursiva(t,lista,sublista,suma,n,pos,pos2):
    if(suma==t):
        print(sublista)
        pos2=0
        sublista=[]
        suma=0
    for i in range(pos,n):
        candidato=lista[i]
        if((suma+candidato)<=t):
            sublista.append(candidato)
            suma+=candidato
            suma_recursiva(t,lista,sublista,suma,n,i+1,pos2+1)
suma_recursiva(6,[6,4,3,3,2,2,2],[],0,7,0,0)