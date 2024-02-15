#1

def ex1():
    list = ['Karol','Adam', 'Marlena', 'Beata']
    
    list.sort()
    print(list)

    list.append('Maciek')
    list.append('Jolanta')

    person = list.pop()
    print(person)

    list.insert(3, "Marta")
    print(list)

    list2 = list.reverse()

    print(list*2)

#2
def ex2():
    string = 'Rzeszów jest piękny'

    print(string[0])
    print(string[6])
    print(string[12])
    print(string[1])

#3
def ex3():
    string = 'Python jest super'

    print(string[0], string[-1])
    print(string[::2])
    print(string[1::3])
    print(string[10::])
    print(string[::-1])

#4
def ex4():
    name = input('Podaj imie: ')
    print(f'Witaj {name}')

    age = input('Podaj wiek: ')
    print(f'Twój wiek to: {age}')

    fullname = []
    fullname.append(input('Podaj imie: '))
    fullname.append(input('Podaj nazwisko: '))
    print(f'{fullname[0][0]}{fullname[1][0]}')

    string = input('Wpisz: ')
    print(string*5)


    string1 = input('Wpisz: ')
    string2 = input('Wpisz: ')
    string3 = string1 + string2
    print(string3)


    string1 = input('Wpisz: ')
    string2 = input('Wpisz: ')
    string3 = string1[:int(len(string1)/2)] + string2[int(len(string1)/2):]
    print(string3)

#RUN
ex1()
ex2()
ex3()
ex4()