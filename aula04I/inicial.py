# SOLID (S) - Responsabilidade Única
class SistemaCadastral:
    def cadastrar(self, nome: str, idade: int) -> None:
        if isinstance(nome, str) and isinstance(idade, int): #1
            print("Acessando o banco de dados....") #2
            print(f"Cadastrar Usuario {nome}, idade {idade}")
        else:
            print("Dados Invalidos") #3