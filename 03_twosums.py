target = 9
numeros = [2,7,11,15]
indices = []
primeiro_num = None

for i in range(len(numeros)): 
    primeiro_num = numeros[i] 
    faltante = 9 - numeros[i] 
    for x in range(len(numeros)): 
        if numeros[x] == faltante and x not in indices: 
            indices.append(i)
            indices.append(x)

print(indices)
