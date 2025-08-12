import turtle
from turtle import Turtle

# Classe base Figura
class Figura:
    def __init__(self, cor, tamanho, x, y):
        self.c = cor                  # Cor 
        self.tamanho = tamanho        # Tamanho
        self.x = x                    # Posição X
        self.y = y                    # Posição Y
        self.t = turtle.Turtle()     
        self.t.color(cor)

    def desenhar(self):
        pass  


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
    print('5- Todas as formas geometricas')


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

elif escolha == '5':
    print('Círculo')
    cor1 = input('Qual a cor: ')
    tamanho1 = float(input('Qual o tamanho: '))
    x1 = float(input('Qual a posição x: '))
    y1 = float(input('Qual a posição y: '))
    figura = circulo(cor1, tamanho1, x1, y1)
    figura.desenhar()
    print('Triângulo')
    cor2 = input('Qual a cor: ')
    tamanho2 = float(input('Qual o tamanho: '))
    x2 = float(input('Qual a posição x: '))
    y2 = float(input('Qual a posição y: '))
    figura = triangulo(cor2, tamanho2, x2, y2)
    figura.desenhar()
    print('Quadrado')
    cor3 = input('Qual a cor: ')
    tamanho3 = float(input('Qual o tamanho: '))
    x3 = float(input('Qual a posição x: '))
    y3 = float(input('Qual a posição y: '))
    figura = quadrado(cor3, tamanho3, x3, y3)
    figura.desenhar()
    print('Hexágono')
    cor4 = input('Qual a cor: ')
    tamanho4 = float(input('Qual o tamanho: '))
    x4 = float(input('Qual a posição x: '))
    y4 = float(input('Qual a posição y: '))
    figura = hexagono(cor4, tamanho4, x4, y4
                      )
    figura.desenhar()

    

else:
    print('Opção inválida.')

turtle.done()
