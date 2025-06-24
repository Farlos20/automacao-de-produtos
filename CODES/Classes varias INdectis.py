class celular:
    def __init__(self,Marca,Preço,Memoria):
        self.Marca = Marca
        self.preço = Preço
        self.Memoria = Memoria
Criar_CLL = input(" Criador de cLL COLOQUE Marca,Preço e memoria ")
Marca,Preço,Memoria = Criar_CLL.split(",")
Criação = celular(Marca,Preço,Memoria)
print(Criação.Memoria)
print(f"Sua Marca é {Criação.Marca}")

