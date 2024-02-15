#1

def ex1():
    for i in range(1, 101):
        print(i)

    for i in range(100, -1, -1):
        print(i)

    for i in range(7, 78, 7):
        print(i)

    for i in range(20, -1, -2):
        print(i)


#2
def ex2():
    astCount = int(input("Podaj liczbe: "))

    for i in range(0, astCount):
        print('*'*astCount)

#3
def ex3():
    astCount = int(input("Podaj liczbe: "))

    for i in range(astCount):
        print(' * '*(i+1))

    for i in range(astCount):
        print('   '*(int((astCount*3-(i+1))/2)), end=" ")
        print(' * ' * (i + 1))

#4
def ex4():
    n = int(input("podaj n: "))
    a = int(input("podaj a: "))
    r = int(input("podaj r: "))

    for i in range(1, n+1):
        print(a+(i-1)*r)

    m = -1
    if r > 0:
        m = 1
    elif r == 0:
        print("Ciag jest staly")
        return

    for i in range(a, a+(n-1)*r+m,r):
        print(i)

#RUN
ex1()
ex2()
ex3()
ex4()