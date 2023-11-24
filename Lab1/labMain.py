import math
from eEx1Helpers import *

#1
def ex1():
    age = int(input("Podaj wiek: "))
    price = 0

    if 4 <= age <= 18:
        price = 10
    elif age > 18:
        price = 20

    print(f"Cena biletu: {price}zl")

#2
def ex2():
    inp = input("Podaj znak:")
    char = ord(' ')
    
    if len(inp) > 0:
        char = ord(inp[0])


    if ord('a') <= char <= ord('z'):
        print("podano mala litere")
    elif ord('A') <= char <= ord('Z'):
        print("podano duza litere")
    else:
        print("Nie podano litery")


def ex3():
    print('1) dodawanie\n2) odejmowanie\n3) mnożenie\n4) dzielenie\n5) potęgowanie')
    
    oper = int(input('Podaj numer operacji: '))
    a = float(input("Podaj liczbe 1: "))
    b = float(input("Podaj liczbe 2: "))
    
    if oper == 1:
        print(f'{a}+{b}={a+b}')
    elif oper == 2:
        print(f'{a}-{b}={a-b}')
    elif oper == 3:
        print(f'{a}*{b}={a*b}')
    elif oper == 4:
        if b != 0:
            print(f'{a}/{b}={a/b}')
        else:
            print('nie dziele przez 0, tak juz mam :D')
    elif oper == 5:
        print(f'{a}^{b}={a**b}')

def ex4():
    print('ax^2+bx+c=0')
    
    a = float(input("Podaj a: "))
    b = float(input("Podaj b: "))
    c = float(input("Podaj c: "))
    
    delta = b**2 - 4*a*c
    
    if delta < 0:
        print("brak rozwiazan")
    elif delta == 0:
        print(f'x={-b/2*a}')
    else:
        sqrtDelta = math.sqrt(delta)
        print(f'x1={(-b-sqrtDelta)/2*a}')
        print(f'x2={(-b+sqrtDelta)/2*a}')
  
def ex5():
    x = int(input("Podaj x: "))
    y = int(input("Podaj y: "))
    z = int(input("Podaj z: "))
    
    if x > y:
        x, y = y, x
    
    if y > z:
        y, z = z, y
    
    if x > y:
        x, y = y, x
        
    print(f"{x} {y} {z}")

def eEx1():
    x = float(input("Podaj x: "))

    print(f'a(x)={a(x)}')
    print(f'b(x)={b(x)}')
    print(f'c(x)={c(x)}')

def eEx2():
    rain = bool(int(input("Czy pada deszcz? 1/0: ")))
    bus = bool(int(input("Czy jest autobus? 1/0: ")))

    if rain and bus:
        print("Weź parasol, Dostaniesz się na uczelnie")
    elif rain and not bus:
        print("Nie dostaniesz się na uczelnię")
    elif not rain and bus: 
        print("Dostaniesz się na uczelnie, Miłego dnia i pięknej pogody")

def eEx3():
    inp = input("Podaj litere:")
    letter = ord(' ')
    
    if len(inp) > 0:
        letter = ord(inp[0])
    
    if ord('a') <= letter <= ord('z'):
        print(chr(int(letter)-32))
    elif ord('A') <= letter <= ord('Z'):
        print(chr(int(letter)+32))
    else:
        print("Nie podano litery")

#RUN
# ex1()
# ex2()
# ex3()
# ex4()
# ex5()
# eEx1()
# eEx2()
# eEx3()
