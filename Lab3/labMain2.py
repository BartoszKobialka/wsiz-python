#2

def ex2():
    shopList = {"czekolada": 8, "stek": 70, "hugo spritz": 20}

    print(shopList)

    print(sum(shopList.values()))

    s = 0

    for (k, el) in enumerate(shopList):
        s += int(k)
    
    print(s)

def ex3():
    payMap = {'wrzesień': 50, 'październik': 65, 'listopad': 55, 'grudzień': 70}

    print(f'suma: {sum(payMap.values())}')
    print(f'min: {min(payMap.values())}')
    print(f'max: {max(payMap.values())}')
    avg = sum(payMap.values())/len(payMap)
    print(f'srednia: {avg}')

    if payMap['grudzień'] > avg:
        print('Zaczmij oszczędzać')

#RUN
ex2()
ex3()