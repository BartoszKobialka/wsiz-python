import random 
import math
import time
import datetime
import keyword

#1
def ex1():
    # zakładam ilosc osób w grupie na 15
    luckyNumber = random.randint(1, 15)
    print(f"Szczęśliwy numerek: {luckyNumber}")
    
    annuals = [1999, 2000, 2001, 2002, 2003]
    print(f"Szczęśliwy rocznik {random.choice(annuals)}")
    
    lottoNumbers = []
    for i in range(49):
        lottoNumbers.append(i+1)
    
    print(f"Wynik lotto: {random.sample(lottoNumbers,6)}")
    
#2
def ex2():
    print(f"√81 = {math.sqrt(81)}")
    print(f"8^10 = {8**10}")
    print(f"√2 + √3 + √6 = {math.sqrt(2) + math.sqrt(3) + math.sqrt(6)}")
    print(f"√-5 = {complex(0, math.sqrt(5))}")
    print(f"(3)√125 = {math.pow(125, 1/3)}")
    
#3
def ex3():
    timeForWait = int(input("Podaj czas w sekundach: "))
    
    while timeForWait > 0:
        print("Pozostało sekund:", timeForWait)
        time.sleep(1)  
        timeForWait -= 1
    print("Koniec czasu!")
    
#4
def ex4():
    print(f"Od ostatnich laboratoriów upłyneło {(datetime.datetime.now() - datetime.datetime(2024, 2, 11)).days} dni")
    
#5
def ex5():
    words = ["for", "print", "break", "done", "bad"]
    
    for word in words:
        if keyword.iskeyword(word):
            print(f"{word} jest słowem kluczowym")
        else:
            print(f"{word} nie jest słowem kluczowym")

#6
def ex6():
    print(dir(math))
    print(dir(tuple))
    print(dir(keyword))
    
#7
def ex7():
    begin = int(input("Podaj start: "))
    end = int(input("Podaj koniec: "))
    
    numbers = []
    
    for i in range(10):
        numbers.append(random.randint(begin, end))
    
    numbers = tuple(numbers)
    
    sumOfNumbers = 0
    
    for i in numbers:
        sumOfNumbers += i
        
    print(f"Średnia {sumOfNumbers/len(numbers)}")
        
#8
def ex8(a, b, alfa):
    if alfa <= 0 or alfa >= 90:
        return "Kąt musi byc osty"
    
    if a <= 0 or b <= 0:
        return "Długości boków muszą byc > 0"
    
    rad = math.radians(alfa)  
    area = 0.5 * a * b * math.sin(rad)
    return f"Pole trójkąta: {area}"
    
#9
def ex9():
    begin = int(input("Podaj start: "))
    end = int(input("Podaj koniec: "))
    
    toGuess = random.randint(begin, end)
    
    for i in range(3):
        guess = int(input("Podaj liczbę: "))
        
        if guess > toGuess:
            print("za duzo")
        elif guess < toGuess:
            print("za mało")
        else:
            print("Brawo!")
            break
     
#10
def ex10():
    year = int(input("Podaj rok: "))
    month = int(input("Podaj miesiąc: "))
    day = int(input("Podaj dzień: "))
    
    date = datetime.datetime(year, month, day)
    
    daysDelta = (date - datetime.datetime(year, 1, 1)).days
    
    print(f"Dzień w roku: {daysDelta}")
    print(f"Numer tygodnia: {math.ceil(daysDelta/7)}")
    print(f"{(date - datetime.timedelta(days=14)).date()} {(date + datetime.timedelta(days=14)).date()}")
    print(f"Najblizsza niedziela: {(date + datetime.timedelta(days=(6 - date.weekday()) % 7)).date()}")
    now = datetime.datetime.now()
    now = now.replace(year=date.year, month=date.month, day=date.day)
    
    print(now.timestamp())
        
     
#RUN
ex1()
ex2()
ex3()
ex4()
ex5()
ex6()
ex7()
print(ex8(5, 7, 30))
ex9()
ex10()