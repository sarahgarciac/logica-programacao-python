indices = [] 
palavra = "banana"

for i in range(len(palavra)): 
    if palavra[i] == "a": 
        indices.append(i)

print(f"Aparece 'a' em 'BANANA' nos seguintes indices: {indices}")
