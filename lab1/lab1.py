with open('lab1.txt', 'r') as f:
	adjMatrix = [[int(num) for num in line.split(',')] for line in f]
	for row in adjMatrix:
		print (row)
	print ()
	setMatrix = []
for i in range(0,len(adjMatrix)):
	setMatrix.append([i])



def combine(e):
	e0 = -1
	e1 = -1
	for i in range(0,len(setMatrix)):
		if e[0] in setMatrix[i]:
			e0 = i
		if e[1] in setMatrix[i]:
			e1 = i
	setMatrix[e0] += setMatrix[e1]
	del setMatrix[e1]



while (len(setMatrix) > 1):
	edges = []
	for component in setMatrix:
		m = [999,[0,0]]
		for vertex in component:
			for i in range(0,len(adjMatrix[0])):
				if i not in component and adjMatrix[vertex][i] != 0:
					if (m[0] > adjMatrix[vertex][i]):
						m[0] = adjMatrix[vertex][i]
						m[1] = [vertex,i]
		if (m[1][0] > m[1][1]):
			m[1][0], m[1][1] =  m[1][1],m[1][0]
		if (m[1] not in edges):
			edges.append(m[1])
	for e in edges:
		combine(e)
	print("Зв’язки: " + str(edges) + " Групи: " + str(setMatrix))


