class Pessoa:
 
    def __init__(self, nome: str, idade: int, cpf: str) -> None:
        self.nome = nome
        self.idade = idade
        self.__cpf = cpf

    def andar(self):
        print('Estou Caminhando')

    def __get_cpf(self) -> str:
        return self.__cpf

    def beber(self, bebida) -> None:
        if bebida == 'cerveja':
            print(f'CPF: {self.__get_cpf()}')
            print(f'Bebendo {bebida}')
        else:
            print(f'Bebendo {bebida}')


pessoa = Pessoa('Danilo', 30, '54849a4d6a645')

pessoa.andar()
pessoa.beber('coca-cola')
pessoa.beber('cerveja')
