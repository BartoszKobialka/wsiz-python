
#WHILE
#1

def ex1():
    a = int(input("Podaj liczbe 1:"))
    b = int(input("Podaj liczbe 2:"))

    if a == b:
        print("Liczby sa rowne")
        return None

    if a > b:
        a,b = b,a

    while a <= b:
        print(a)
        a+=1

#2
def ex2():
    for i in range(-8, 9):
        x = i/2
        print(2*x**2-5*x-8)

#3
def ex3():
    while True:
        a = int(input("Podaj liczbe:"))

        if a < 0:
            print("Podales liczbe ujemna")
            break

#4
def ex4():
    a = int(input("Podaj liczbe 1:"))
    b = int(input("Podaj liczbe 2:"))

    if a == b:
        print("Liczby sa rowne")
        return None

    if a > b:
        a, b = b, a

    while a <= b:
        if a % 2 == 0:
            print(a)
        a += 1

# RUN
ex1()
ex2()
ex3()
ex4()