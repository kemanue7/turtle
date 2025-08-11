from turtle import Turtle

t = Turtle()
#menu inicial com as escolhas de desenhos
def menu():
    print('Escolha uma opção:')
    print('1 - Círculo')
    print('2 - Triângulo')
    print('3 - Quadrado')
    print('4 - Hexágono')

#funçao do desenho do circulo
def circulo():
    t.penup()
    t.goto(150, 100)
    t.pendown()
    for _ in range(360):
        t.forward(1)
        t.left(1)
        
#funçao do desenho do triangulo
def triangulo():
    t.penup()
    t.goto(100, 100)
    t.pendown()
    for _ in range(3):
        t.forward(100)
        t.left(120)
        
#funçao do desenho do quadrado
def quadrado():
    t.penup()
    t.goto(0, 100)
    t.pendown()
    for _ in range(4):
        t.forward(100)
        t.left(90)
        
#funçao do desenho do hexagono
def hexagono():
    t.penup()
    t.goto(-100, 100)
    t.pendown()
    for _ in range(6):
        t.forward(100)
        t.left(60)

#funçao de escolha da forma geometrica
menu()
escolha = input("Digite a opção: ")

if escolha == '1':
    print('Círculo')
    circulo()
elif escolha == '2':
    print('Triângulo')
    triangulo()
elif escolha == '3':
    print('Quadrado')
    quadrado()
elif escolha == '4':
    print('Hexágono')
    hexagono()
else:
    print('Opção inválida.')

t.done()

