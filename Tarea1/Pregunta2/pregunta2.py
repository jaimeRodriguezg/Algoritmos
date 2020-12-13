def adyacentes(posicion,max_x,max_y): #Devuelve los vecinos adyacentes a la posicion dada, dentro de los limites de la matriz
	resultado=list()
	i=posicion[0]
	j=posicion[1]
	x=i-1
	y=j-1
	for pos1 in range(x,x+3):
		for pos2 in range(y,y+3):
			if pos1>=0 and pos2>=0 and (pos1,pos2)!=posicion and pos1<max_x and pos2<max_y:
				resultado.append((pos1,pos2))
	return resultado
def BFS_modificado(matriz,posicion): #Marca los visitados en busqueda a lo ancho pero solo los que son "W"
	visitados=list()
	vecinos_no_visitados=list()
	cola=list()
	cola.append(posicion)
	while len(cola)!=0:
		x=cola[0]
		i=x[0]
		j=x[1]
		del cola[0]
		if (x not in visitados) and matriz[i][j]=="W":
			visitados.append(x)
			vecinos=adyacentes(x,len(matriz),len(matriz[0]))
			for y in vecinos:
				i=y[0]
				j=y[1]
				if (y not in visitados) and matriz[i][j]=="W":
					vecinos_no_visitados.append(y)
			while len(vecinos_no_visitados)!=0:
				y=vecinos_no_visitados[0]
				del vecinos_no_visitados[0]
				cola.append(y)
	return(len(visitados))
def terrenos_inundados(matriz,consultas): #realiza las consultas respecto a la matriz llamando al algoritmo por cada consulta
	for consulta in consultas:
		print(BFS_modificado(matriz,consulta))
	print("")
cant_casos = int(input("").strip())
input("").strip()
contador=0
matrix=list()
consultas=list()
while(contador!=cant_casos):
	linea=input("").strip()
	if len(linea)>0:
		if linea[0]=="W" or linea[0]=="L":
			matrix.append(linea)
		else:
			consulta=linea.strip().split()
			x=int(consulta[0])
			y=int(consulta[1])
			consultas.append((x-1,y-1))
	else:
		contador+=1
		terrenos_inundados(matrix,consultas)
		matrix=list()
		consultas=list()