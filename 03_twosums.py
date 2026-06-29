target = 9
numeros = [2,7,11,15]
indices = []
primeiro_num = None

for i in numeros: 
    primeiro_num = i 
    faltante = 9 - i 
    for x in numeros: 
        if x == faltante and x not in indices: 
            indices.append(i)
            indices.append(x)

print(indices)
