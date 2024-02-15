import math

#1
def ex1(radius):
    area = math.pi * radius ** 2
    print("Pole koła:", area)

#2
def ex2(a, b, h):
    area = (a + b) / 2 * h
    print("Pole trapezu:", area)

#3
def ex3(name, age=20):
    """Funkcja wypisuje imie i wiek"""
    print("Imię:", name, "Wiek:", age)
    print(__doc__)
    
#4
def ex4(number):
    if number > 0:
        print(number, "jest dodatni.")
    else:
        print(number, "nie jest dodatni.")
        
#5        
def ex5(weight, height):
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        print("BMI:", bmi, "- niedowaga")
    elif bmi < 25:
        print("BMI:", bmi, "- waga normalna")
    elif bmi < 30:
        print("BMI:", bmi, "- nadwaga")
    else:
        print("BMI:", bmi, "- otyłość")

#6
def ex6(a, b, c):
    semiPerimeter = (a + b + c) / 2
    area = math.sqrt(semiPerimeter * (semiPerimeter - a) * (semiPerimeter - b) * (semiPerimeter - c))
    print("Pole trójkąta:", area)
    return area

#7
def ex7(text):
    reversedText = text[::-1]
    print("Odwrotny tekst:", reversedText)
    return reversedText

#8
def ex8(base, exponent):
    if exponent == 0:
        return 1
    
    return base * ex8(base, exponent-1)

#9
def ex9(n):
    if n == 0:
        return 0
    
    if n == 1:
        return 1
        
    return ex9(n-1) + ex9(n-2)

def eEx1(name):
    if name[-1] == 'a':
        print(name, "jest kobietą")
    else:
        print(name, "jest mężczyzną")

def eEx2(*values):
    max_value = max(values)
    return max_value

def eEx3(a, b=0, c=0):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
       return ()
    elif discriminant == 0:
        x = -b / (2*a)
        return (x,)
    else:
        x1 = (-b - math.sqrt(discriminant)) / (2*a)
        x2 = (-b + math.sqrt(discriminant)) / (2*a)
        return x1,x2

# RUN
ex1(5)
ex2(3, 4, 5)
ex3("Jan", 25)
ex3("Ania")
ex4(10)
ex4(-5)
ex5(70, 1.75)
ex6(3, 4, 5)
ex7("kajak")
print("Wynik potęgi:", ex8(2, 3))
print("Fib " ,ex9(7))
eEx1("Kasia")
eEx1("Marcin")
print("Maksymalna wartość:", eEx2(1, 2, 3, 56, 7))
print(eEx3(1, -3, 2))
print(eEx3(1, 3, 4))
print(eEx3(1, 0, 0))
