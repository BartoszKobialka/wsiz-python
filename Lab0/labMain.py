import random
import math

#1 
# + operator dodawania 
# - operator odejmowania
# / operator dzielenia
# // dzielenie całkowite
# % reszta z dzielenia
# ** potęgowanie
# 

#2 
# int(3.0) -> 3 przekształca argument w liczę całkowitą, w tym przypadku "odcinając" częśc dziesiętną
# float(3) -> 3.0 przekształca argument w liczę rzeczywistą
# float("3") -> 3.0 przekształca argument w liczę rzeczywistą, w tym przypadku argumentem jest ciąg znaków mozliwy do przekształcenia
# str(12.4) -> "12.4" przekształca argument w ciąg znaków
# bool(0) -> False przekształca argument w wartośc logiczną
# 

#3
def ex3():
    x = int(input("Podaj dlugosc: "))
    y = int(input("Podaj wysokosc: "))

    print(f'Pole: {x*y} Obwod: {2*(x+y)}')

#4
def ex4():
    distance = random.randint(1, 100000)
    avgFuelUsage = float(input("Podaj srednie spalanie: "))

    fuelUsed = avgFuelUsage * distance / 100

    print(f'Przejechano {distance}km')
    print(f'Spalono: {fuelUsed}l \n Przewidywany koszt {(fuelUsed * 6.5):.2f}zł')

#Extra
#1

def eEx1():
    print('0=ax+b')
    
    a = float(input("Podaj a: "))
    b = float(input("Podaj b: "))
    
    if a == 0:
        print('sprzeczne')
    else:
        print(f'Wynik: x={-b/a}')

def eEx2():
    a = float(input("Podaj a: "))
    b = float(input("Podaj b: "))
    c = float(input("Podaj c: "))

    p = (a+b+c)/2
    P = math.sqrt(p*(p-a)*(p-b)*(p-c))
    
    print(f'Pole: {P}')
    
def eEx3():
    a = float(input("Podaj liczbe 1: "))
    b = float(input("Podaj liczbe 2: "))
    
    print(f'{a}+{b}={a+b}')
    print(f'{a}-{b}={a-b}')
    print(f'{a}*{b}={a*b}')
    
    if b != 0:
        print(f'{a}/{b}={a/b}')
    else:
        print('nie dziele przez 0, tak juz mam :D')

#RUN
#ex3()
#ex4()
#eEx1()
#eEx2()
#eEx3()
