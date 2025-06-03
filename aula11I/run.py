class Mamifero:
    def __init__(self, localizacao: str) -> None:
        self.localizacao = localizacao
        self._tamanho = 1.23

    def andar(self) -> None:
        print(f"O Animal esta andando pelo {self.localizacao}")

    def _dormir (self) -> None:
        print("O Animal esta dormindo")

class Gato(Mamifero):
    def __init__(self, localizacao: str) -> None:
        super().__init__(localizacao)

    def miar(self) -> None:
        print("O Gato esta miando")
        self._dormir()
        print(self._tamanho)

cat = Gato("Argentina")
cat.miar()
