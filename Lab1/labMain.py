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
    char = chr(input("Podaj znak"))

    if chr('a') <= char <= chr('z'):
        print("podano mala litere")
    elif chr('A') <= char <= chr('Z'):
        print("podano duza litere")
    else:
        print("Nie podano litery")


#RUN
ex1()