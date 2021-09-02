class Pessoa:
    olhos = 2  # atributo de classe

    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Hi {id(self)}'

    @staticmethod  # decor@tors
    def metodo_estatico():
        return 42

    @classmethod  # decor@tors
    def metodo_de_classe(cls):
        return cls.olhos


if __name__ == '__main__':
    pai = Pessoa('Marjorie Ann', nome='Marcos Ranes', idade=35)
    filho = Pessoa(nome='Marjorie Ann', idade=1)
    print(pai.cumprimentar())
    for name in pai.filhos:
        print(name)
    print(f'{pai.__dict__}')
    print(f'{filho.__dict__}')
    print(f'{id(Pessoa.metodo_estatico())}')
    print(f'{id(pai.metodo_estatico())}')
    print(f'{pai.olhos}')
    print(f'{Pessoa.metodo_de_classe()}')
    print(f'{Pessoa.__dict__}')
