import random

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

#RUN
# ex3()
ex4()

