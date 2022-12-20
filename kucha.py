import random
import csv
def _1_1():
    print('Hello, World')
def _1_2():
    x = 'BOOBA???????!!!!!!'
    print(x)
def _2_1():
    print('"BIBA"')
def _2_2():
    print("'BOBA'")
def _2_3():
    print('''BIBA
    BOBA
    BIBA
    BOBA''')
def _2_4():
    print('BIBA'
          'BOBA'
          'BIBA'
          'BOBA')
def _3_1(x=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], y=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]):
    print(x)
def _3_2(x=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], y=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]):
    print(len(x))
def _3_3(x=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], y=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]):
    print(x + y)
def _3_4(x=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], y=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]):
    print(x + [' '] + y)
def _3_4(x=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], y=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]):
    print('bazigna'[2:6])
def _4_1():
    x = str
    x = input('введите чо-нить:')
def _4_2():
    x = str
    x = input('введите чо-нить:')
    x = x.lower()
    print({x})
def _4_3():
    x = str
    x = input('введите чо-нить:')
    x = x.lower()
    print(len(x))
def _5_1():
    x = str(random.randint(0, 100))
    print(type(x), x)
    x = int(x) * random.randint(0, 100)
    print(type(x), x)
def _5_2():
    x = str(random.uniform(0, 100))
    print(type(x), x)
    x = float(x) * random.uniform(0, 100)
    print(type(x), x)
def _5_3():
    y = 'boba - '
    x = str(random.uniform(0, 100))
    print(y + str(x))
def _5_4():
    x = float(input('введи число:'))
    y = float(input('введи число опять:'))
    print(f'The product of {x} and {y} is {y * x}.')
def _6_1():
    weight = 0.2
    animal = 'newt'
    print(str(weight) + ' kg is weight of the ' + animal)
def _6_2():
    weight = 0.2
    animal = 'newt'
    print(f'{weight} kg is weight of the {animal}')
def _7_1(a = 'AAA'):
    print(a.find('a'))
def _7_2(a = 'Somebody said something to Samantha.'):
    print(a.replace('s', 'x'))
def _7_3():
    a = input('Ну и где мой текст? ')
    print(a.find(input('Что ищем? ')))
def _8_1():
    print(round(float(input('Enter a number: ')), 2))
def _8_2():
    print('The absolute number: ', abs(float(input('Enter a number: '))))
def _8_3():
    a = float(input('Enter а number: '))
    b = float(input('Enter another number: '))
    # print(f'The difference between {a} and {b} is an integer? {isinstance(abs(a-b), int)}', end='')
    print(f'The difference between {a} and {b} is an integer? ', end='')
    if abs(a - b) == int(abs(a - b)):
        print(True)
        return True
    else:
        print(False)
        return False
def _8_4():
    a = float(input('Enter а number: '))
    b = float(input('Enter another number: '))
    # print(f'The difference between {a} and {b} is an integer? {isinstance(abs(a-b), int)}', end='')
    print(f'The difference between {a} and {b} is an integer? ', end='')
    if abs(a - b) == int(abs(a - b)):
        print(True)
        return True
    else:
        print(False)
        return False
def _9_1(a=3, b=0.125):
    print(f'{a}^{b} = ', round(a ** b, 3))
def _9_2(a=150000):
    a=str(int(a))
    a=a[::-1]
    a_r=str('')
    c=0
    for i in a:
        c+=1
        if (c/3)==int(c/3):
            a_r+=i+' '
        else:
            a_r+=i
    a_r=a_r[::-1]+'.00'
    return a_r
def _9_3(a=2, b=10):
    print(f'{int(a / b * 100)}%')
def cube(a):
    return a**3
def greet(a):
    return f'Hello {a}!'
def _11_1(a=10):
    for i in range(a-1):
        print(i+2)
def _11_2(a=10):
    b=2
    while b!=a+1:
        print(b)
        b+=1
def doubles(a):
    return a*2
def _11_3(a ,b=3):
    for i in range(b):
        a=doubles(a)
        print(a)
def _12_1(a=5):
    b=input('введите слово: ')
    if len(b)==a:
        print(f'Длинна ввода составляет {a} символов')
    elif len(b)>a:
        print(f'Длинна ввода больше {a} символов')
    else:
        print(f'Длинна ввода меньше {a} символов')
def _12_2(a=3, b=1, c=10):
    print(f'Я загадал(а) число от {b} до {c}. Угадайте его: ', end='')
    if a==float(input()):
        print('Вы победили! ^_^')
    else:
        print('Вы проиграли... Обидно, наверное, АХАХАХАХАХАХАХАХАХАХАХАХА')
def _13_1(a='q', b='Q'):
    d=1
    while d!=0:
        c=input('Введите букву: ')
        if c==a or c==b:
            break
    print('Ладно, свободен)))')
def _13_2(a=1, b=50):
    for i in range(abs(a-b)+1):
        if (a+i)/3==int((a+i)/3):
            continue
        else:
            print(a+i, end=', ')
def _14_1():
    d=1
    while d!=0:
        a=float(input('Введите целое число: '))
        if a==round(a):
            a=int(a)
            break
        else:
            print('Try again')
    return a
def _14_2(a=5):
    d=1
    c=[]
    while d!=0:
        b=float(input('Введите целое число: '))
        if b==round(b) and b<a and b>=-a:
            b=int(b)
            break
        elif b>=a:
            print('Слишком большое число')
        elif b<-a:
            print('Слишком маленькое число')
        else:
            print('Число не целое')
    print(f'Введите последовательно {a} чисел: ')
    for i in range(a):
        c.append(input(f'Осталось {a-i} чисел '))
    return c[b]
def _15_1():
    return ('first', 'second', 'third')
def _15_2(b=1, a=('first', 'second', 'third')):
    return a[b]
def _15_3():
    cardinal_numbers=('first', 'second', 'third')
    position1=cardinal_numbers[0]
    position2=cardinal_numbers[1]
    position3=cardinal_numbers[2]
    print(position1)
    print(position2)
    print(position3)
def _15_4(a='andrey'):
    a=tuple(a)
    return a
def _15_5(a='x', b='andrey'):
    b=tuple(b)
    return a in b
def _15_6(a=0, b='andrey'):
    b=tuple(b)
    c=[]
    for i in range(len(b)):
        if a!=i:
            c.append(b[i])
    return tuple(c)
def _16_1(a='rice', b='beans'):
    c=[a, b]
    return c
def _16_2(a='broccoli', b=['rice', 'beans']):
    b.append(a)
    return b
def _16_3(a='bred', b='pizza', c=['rice', 'beans', 'broccoli']):
    c.extend([a, b])
    return c
def _16_4(a=2, b=['rice', 'beans', 'broccoli', 'bred', 'pizza']):
    for i in range(a):
        print(b[i], end=', ')
def _16_5(a=-1, b=['rice', 'beans', 'broccoli', 'bred', 'pizza']):
    print(b[a])
def _16_6(a='eggs, fruit, orangejuice'):
    return a.split(', ')
def _16_7(a=['eggs', 'fruit', 'orangejuice']):
    print(len(a))
    return len(a)
def _16_8(a=['eggs', 'fruit', 'orangejuice']):
    b=[]
    for i in a:
        b.append(len(i))
    print(b)
    return b
def _17_1(a=(1, 2), b=(3,4)):
    c=(a, b)
    print(c)
    return c
def _17_2(a=((1, 2), (3, 4))):
    for i in range(len(a)):
        b=0
        for k in a[i]:
            b+=k
        print(f'Row {i+1} sum: {b}')
def _17_3(a=4, b=3, c=2, d=1):
    numbers=[a, b, c, d]
    print(numbers)
    return numbers
def _17_4(a=[4, 3, 2, 1]):
    b=a[:]                      #?
    print(b)
    return b
def _17_5(a=[4, 3, 2, 1]):
    a.sort()
    print(a)
    return a
def enrollment_stats(universities=[
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]):
    a=[]
    b=[]
    for i in universities:
        a.append(float(i[1]))
        b.append(float(i[2]))
    return a, b
def mean(a=enrollment_stats(),universities=[
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]):
    return round(sum(a[0])/len(universities), 2), round(sum(a[1])/len(universities), 2)
def SS(a=enrollment_stats(), b=mean()):
    print(f'''************************
Total students: {int(sum(a[0]))}
Total tuition: {_9_2(sum(a[1]))} dollar
Students mean {int(b[0])}
Tuition mean: {_9_2(b[1])} dollar
************************''')
def convert_cel_to_far(a):
    return a*9/5+32
def convert_far_to_cel(a):
    return (a-32)*5/9
def temp():
    a = float(input('Enter а temperature in degrees F: '))
    print(f'{a} degrees F = {round(convert_far_to_cel(a), 2)} degrees C')
    a = float(input('Enter а temperature in degrees C: '))
    print(f'{a} degrees C = {round(convert_cel_to_far(a), 2)} degrees F')
def _18_1():
    a={}
    print(a)
    return a
def _18_2(a='Enterprise', b='Picard', c='Voyager', d='Janeway', e='Defiant ', f='Sisko'):
    g={}
    g[a]=b
    g[c]=d
    g[e]=f
    print(g)
    return g
def _18_3(a=['Enterprise', 'Discovery'],b={'Enterprise': 'Picard', 'Voyager': 'Janeway', 'Defiant ': 'Sisko'}):
    for i in a:
        if i in b != True:
            continue
        else:
            b[i]='unknown'
    print(b)
    return b
def _18_4(a={'Enterprise': 'Picard', 'Voyager': 'Janeway', 'Defiant ': 'Sisko', 'Discovery': 'unknown'}):
    for i in a:
        print(f'The {i} is captained by {a[i]}')
def _18_5(a='Discovery', b={'Enterprise': 'Picard', 'Voyager': 'Janeway', 'Defiant ': 'Sisko', 'Discovery': 'unknown'}):
    del b[a]
    print(b)
    return b
def _18_6(a={'Enterprise': 'Picard', 'Voyager': 'Janeway', 'Defiant ': 'Sisko'}, b=('Enterprise', 'Picard'), c=('Voyager', 'Janeway'), d=('Defiant ', 'Sisko')):
    #a=dict(a)
    a=dict([b, c, d])
    print(a)
    return a
def _19_1(a=['Discovery', 'Enterprise', 'Defiant', 'Voyager'], b='zachet.txt'):
    file=open(b, 'w')
    for i in a:
        file.write(i+'\n')
    file.close()
def _19_2(a='zachet.txt'):
    file=open(a, 'r')
    for i in file.readlines():
        print(i[:-2])
    file.close()
def _19_3(b='D', a='zachet.txt'):
    file=open(a, 'r')
    for i in file.readlines():
        if i[0]==b:
            print(i[:-2])
def _20_1(a='zachet.csv', b = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15]
    ]):
    with open(a, mode='w+', encoding='cp1251', newline='') as file:
        writer = csv.writer(file, delimiter='|')
        writer.writerows(b)
def _20_2(a='zachet.csv'):
    with open(a) as file:
        lines = list(csv.reader(file, delimiter='|'))
        for i in range(len(lines)):
            for k in range(len(lines[i])):
                lines[i][k] = int(lines[i][k])
        print(lines)
        return lines
def _20_3(a='zachet.csv', favorite_colors = [
    {"name": "Joe", "favorite_color": "blue"},
    {"name": "Anne", "favorite_color": "green"},
    {"name": "Bailey", "favorite_color": "red"},
    ]):
    b=[]
    c=[]
    e=[]
    with open(a, mode='w+', encoding='cp1251', newline='') as file:
        writer = csv.writer(file, delimiter='|')
        for i in range(len(favorite_colors)):
            c.append([])
            for k in favorite_colors[i]:
                if len(b)!=len(favorite_colors[i]):
                    b.append(k)
                    c[i].append(favorite_colors[i][k])
                else:
                    c[i].append(favorite_colors[i][k])
        writer.writerows([b]+c)
        #print([b] + c)
def _20_4(a='zachet.csv', favorite_colors = [
    {"name": "Joe", "favorite_color": "blue"},
    {"name": "Anne", "favorite_color": "green"},
    {"name": "Bailey", "favorite_color": "red"},
    ]):
    b=[]
    c=[]
    e=[]
    with open(a, mode='w+', encoding='cp1251', newline='') as file:
        writer = csv.writer(file, delimiter='|')
        for i in range(len(favorite_colors)):
            c.append([])
            for k in favorite_colors[i]:
                if len(b)!=len(favorite_colors[i]):
                    b.append(k)
                    c[i].append(favorite_colors[i][k])
                else:
                    c[i].append(favorite_colors[i][k])
        writer.writerows([b]+c)
def _20_5(a='zachet.csv'):
    d=[]
    with open(a) as file:
        lines = list(csv.reader(file, delimiter='|'))
        b, *c=lines
        for i in range(len(c)):
            d.append({})
            for k in range(len(b)):
                d[i][b[k]]=c[i][k]
        print(d)