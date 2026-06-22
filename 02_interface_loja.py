#Você e sua equipe de programadores foram contratados para desenvolver um
#app de vendas para uma loja que vende Açaí e Cupuaçu. Você ficou com a parte de
#desenvolver a interface do cliente para retirada do produto.


print("Boas-vindas, Sarah Garcia de Carvalho!")
print("Cardápio: \n --- TAMANHO | Cupuaçu |    Açaí --- \n ---   P     |  R$9,00 | R$11,00 --- \n ---   M     | R$14,00 | R$16,00 --- \n ---   G     | R$18,00 | R$20,00 ---")
valor = 0 

while True: 
    sabor = input("Escolha o sabor desejado (CP = Cupuaçu e AC = Açaí) \n").upper()
    while sabor != "CP" and sabor != "AC": #se usar or aqui, vai entrar num loop infinito, pq sempre vai ser true - ac é diferente de cp e vice-versa
        print("Sabor inválido, tente novamente!") 
        sabor = input("Escolha o sabor: CP (cupuaçu) ou AC (açai) \n").upper()

    tamanho = input("Escolha o tamanho (P = pequeno, M = médio e G = grande) \n").upper()
    while tamanho != "P" and tamanho != "M" and tamanho != "G": 
        print("Tamanho inválido, tente novamente!")
        tamanho = input("Escolha o tamanho: P, M ou G \n").upper()
    
    if sabor == "AC" and tamanho == "P": #conseguiria usar um def aqui para economizar espaço
        valor += 11.00
        
    elif sabor == "AC" and tamanho == "M": 
        valor += 16.00

        print("Seu pedido vai ficar: R$16,00")
    elif sabor == "AC" and tamanho == "G": 
        valor += 20.00
        
    elif sabor == "CP" and tamanho == "P": 
        valor += 9.00
        
    elif sabor == "CP" and tamanho == "M": 
        valor += 14.00
        
    else: 
        valor += 18.00
        
    mais_algo = input("Deseja mais alguma coisa? S/N \n").upper()
    if mais_algo == "S": 
        continue 
    else:
        print(f"Seu pedido ficou com um valor total de: R${valor}")
        break 
