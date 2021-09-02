

"""
Você deve criar uma classe carro que vai possuir dois atributos compostos por outras duas classes:

Motor
Direção
O Motor terá a responsabilidade de controlar a velocidade.
Ele oferece os seguintes atributos:

Atributo de dade velocidade
Método acelerar, que deverá incrementar a velocidade de uma unidade
Método frear que deverá decrementar a velocidade em duas unidades
A Direção terá a responsabilidade de controlar a direção. Ela oference os seguintes atributos:

Valor de direção com valores possíveis: Norte, Sul, Leste, Oeste.

Metodo girar_a_direita

Metodo girar_a_esquerda

N
O L
S

Exemplo:

    >>>  # Testando motor
    >>> motor = Motor()
    >>> motor.velocidade
    0

    >>> motor.acelerar()
    >>> motor.velocidade
    1

    >>> motor.acelerar()
    >>> motor.velocidade
    2

    >>> motor.acelerar()
    >>> motor.velocidade
    3

    >>> motor.frear()
    >>> motor.velocidade
    1

    >>> motor.frear()
    >>> motor.velocidade
    0

    >>> Testando Direção
    >>> direcao = Direcao()
    >>> direcao.valor
    ‘Norte’

    >>> direcao.girar_a_direita()
    >>> direcao.valor
    ‘Leste’

    >>> direcao.girar_a_direita()
    >>> direcao.valor
    ‘Sul’

    >>> direcao.girar_a_direita()
    >>> direcao.valor
    ‘Oeste’

    >>> direcao.girar_a_direita()
    >>> direcao.valor
    ‘Norte’

    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    ‘Oeste’

    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    ‘Sul’

    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    ‘Leste’

    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    ‘Norte’

    >>> carro = Carro(direcao, motor)
    >>> carro.calcular_velocidade()
    0

    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    1

    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    2

    >>> carro.frear()
    >>> carro.calcular_velocidade()
    0

    >>> carro.calcular_direcao()
    ‘Norte’
    >>> carro.girar_a_direita()
    >>> carro.calcular_direcao()
    ‘Leste’
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    ‘Norte’
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    ‘Oeste’
"""

class Car:
    pass

class Motor:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        self.velocidade -= 2
