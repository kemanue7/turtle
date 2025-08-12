import turtle
from turtle import Turtle

# Classe base Figura
class Figura:
    def __init__(self, cor, tamanho, x, y):
        self.c = cor                  # Cor da forma
        self.tamanho = tamanho        # Tamanho da forma
        self.x = x                    # Posição X
        self.y = y                    # Posição Y
        self.t = turtle.Turtle()      # Objeto turtle para desenho
        self.t.color(cor)

    def desenhar(self):
        pass  # Método genérico a ser sobrescrito nas subclasses


# Função do desenho do círculo
class circulo(Figura):
    def desenhar(self):
        self.t.penup()
        self.t.goto(self.x, self.y)
        self.t.pendown()
        for _ in range(360):
            self.t.forward(self.tamanho)
            self.t.left(1)


# Função do desenho do triângulo
class triangulo(Figura):
    def desenhar(self):
        self.t.penup()
        self.t.goto(self.x, self.y)
        self.t.pendown()
        for _ in range(3):
            self.t.forward(self.tamanho)
            self.t.left(120)


# Função do desenho do quadrado
class quadrado(Figura):
    def desenhar(self):
        self.t.penup()
        self.t.goto(self.x, self.y)
        self.t.pendown()
        for _ in range(4):
            self.t.forward(self.tamanho)
            self.t.left(90)


# Função do desenho do hexágono
class hexagono(Figura):
    def desenhar(self):
        self.t.penup()
        self.t.goto(self.x, self.y)
        self.t.pendown()
        for _ in range(6):
            self.t.forward(self.tamanho)
            self.t.left(60)


# Menu inicial com as escolhas de desenhos
def menu():
    print('Escolha uma opção:')
    print('1 - Círculo')
    print('2 - Triângulo')
    print('3 - Quadrado')
    print('4 - Hexágono')


# Função de escolha da forma geométrica
menu()
escolha = input("Digite a opção: ")

if escolha == '1':
    print('Círculo')
    cor = input('Qual a cor: ')
    tamanho = float(input('Qual o tamanho: '))
    x = float(input('Qual a posição x: '))
    y = float(input('Qual a posição y: '))
    figura = circulo(cor, tamanho, x, y)
    figura.desenhar()

elif escolha == '2':
    print('Triângulo')
    cor = input('Qual a cor: ')
    tamanho = float(input('Qual o tamanho: '))
    x = float(input('Qual a posição x: '))
    y = float(input('Qual a posição y: '))
    figura = triangulo(cor, tamanho, x, y)
    figura.desenhar()

elif escolha == '3':
    print('Quadrado')
    cor = input('Qual a cor: ')
    tamanho = float(input('Qual o tamanho: '))
    x = float(input('Qual a posição x: '))
    y = float(input('Qual a posição y: '))
    figura = quadrado(cor, tamanho, x, y)
    figura.desenhar()

elif escolha == '4':
    print('Hexágono')
    cor = input('Qual a cor: ')
    tamanho = float(input('Qual o tamanho: '))
    x = float(input('Qual a posição x: '))
    y = float(input('Qual a posição y: '))
    figura = hexagono(cor, tamanho, x, y)
    figura.desenhar()

else:
    print('Opção inválida.')

turtle.done()
