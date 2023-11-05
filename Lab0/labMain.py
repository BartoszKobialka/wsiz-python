#3
def ex3():
    x = int(input("Podaj dlugosc: "))
    y = int(input("Podaj wysokosc: "))

    print(f'Pole: {x*y} Obwod: {2*(x+y)}')

#4
def ex4():
    distance = int(input("Podaj dlugosc trasy: "))
    avgFuelUsage = float(input("Podaj srednie spalanie: "))

    fuelUsed = avgFuelUsage * distance / 100

    print(f'Spalono: {fuelUsed}l \n Przewidywany koszt {(fuelUsed * 6.5):.2f}zł')

#RUN
# ex3()
ex4()

