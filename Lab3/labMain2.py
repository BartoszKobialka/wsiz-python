import random
import string

#1
def ex1():
    n = int(input("Podaj n: "))
    x = int(input("Podaj x: "))

    stringsList = []

    for i in range(n):
        lettersCount = random.randint(1, x)
        randomString = ""
        
        for j in range(lettersCount):
            randomString += random.choice(string.ascii_letters)
        
        stringsList.append(randomString)
        
    stringsTuple = tuple(stringsList)
    
    charSum = 0
    
    for item in stringsTuple:
        charSum += len(item)    
    
    print(f"Ilosc znaków {charSum}")
    
    charKSum = 0
    
    for item in stringsTuple:
        charKSum += item.count('k') 
    
    print(f"Ilosc znaków k {charKSum}")
    
    subKTSum = 0
    
    for item in stringsTuple:
        subKTSum += item.count('kt') 
    
    print(f"Ilosc znaków kt {subKTSum}")
    
    s = int(input("Podaj s: "))
    
    longerThanSCount = 0
    
    for item in stringsTuple:
        if len(item) > s:
            longerThanSCount += 1
    
    print(f"Ilosc ciągów dłuzszych niz s {longerThanSCount}")

#2
def ex2():
    shopList = {"czekolada": 8, "stek": 70, "hugo spritz": 20}

    print(shopList)

    print(sum(shopList.values()))

    s = 0

    for (k, el) in enumerate(shopList):
        s += int(k)
    
    print(s)

#3
def ex3():
    payMap = {'wrzesień': 50, 'październik': 65, 'listopad': 55, 'grudzień': 70}

    print(f'suma: {sum(payMap.values())}')
    print(f'min: {min(payMap.values())}')
    print(f'max: {max(payMap.values())}')
    avg = sum(payMap.values())/len(payMap)
    print(f'srednia: {avg}')

    if payMap['grudzień'] > avg:
        print('Zaczmij oszczędzać')

def ex4():
    a = random.randint(3, 7)
    b = random.randint(3, 7)
    
    X = set()
    Y = set()

    for i in range(a):
        X.add(random.randint(0, 10))
        
    for i in range(b):
        Y.add(random.randint(0, 10))
    
    print("Zbiór X:", X)
    print("Zbiór Y:", Y)
    print("a) Czy zbiór X zawiera liczbę 5:", 5 in X)
    print("b) Czy zbiór X jest podzbiorem zbioru Y:", X.issubset(Y))
    print("c) Czy zbiór Y jest podzbiorem zbioru X:", Y.issubset(X))
    print("d) Czy zbiór X jest nadzbiorem zbioru Y:", X.issuperset(Y))
    print("e) Czy zbiór Y jest nadzbiorem zbioru X:", Y.issuperset(X))
    print("f) Suma zbiorów X oraz Y:", X.union(Y))
    print("g) Różnica zbiorów X oraz Y:", X.difference(Y))
    print("h) Różnica zbiorów Y oraz X:", Y.difference(X))
    print("i) Iloczyn zbiorów X oraz Y:", X.intersection(Y))
    print("j) Różnica symetryczna zbiorów X oraz Y:", X.symmetric_difference(Y))
    print("k) Wartość najwyższego elementu w obu zbiorach:", max(max(X, default=0), max(Y, default=0)))

    if X:
        first_element_X = next(iter(X))
        X.remove(first_element_X)
        Y.add(first_element_X)
        print("l) Po usunięciu pierwszego elementu z X i dodaniu go do Y - X:", X, "Y:", Y)

    Y.update(X)
    print("m) Po przekopiowaniu wszystkich elementów z X do Y - X:", X, "Y:", Y)

    X.clear()
    Y.clear()
    print("n) Po wyczyszczeniu - X:", X, "Y:", Y)

#RUN
ex1()
ex2()
ex3()
ex4()