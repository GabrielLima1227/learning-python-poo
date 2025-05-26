class Caneta:
    def __init__(self) -> None:
        self.modelo = ""
        self.__ponta = 0

    def getter_modelo(self) -> str:
        return self.modelo
    def setter_modelo(self, nome: str) -> None:
        self.modelo = nome

    def getter_ponta(self) -> float:
        return self.__ponta    
    def setter_ponta(self, valor: float) -> None:
        self.__ponta = valor


caneta_azul = Caneta()

caneta_azul.setter_modelo("Bic Cristal")
caneta_azul.setter_ponta(0.5)

modelo_caneta = caneta_azul.getter_modelo()
ponta_caneta = caneta_azul.getter_ponta()

print(modelo_caneta)
print(ponta_caneta)
