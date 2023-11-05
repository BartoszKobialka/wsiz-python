#1
def ex1():
    age = int(input("Podaj wiek: "))
    price = 0

    if age >= 4 and age <= 18:
        price = 10
    elif age > 18:
        price = 20

    print(f"Cena biletu: {price}zl")


#RUN
ex1()