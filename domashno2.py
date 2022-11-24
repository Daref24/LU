#1
def square():
    a = float(input("Въведете страна на квадрата: "))
    sqr = a*a
    return sqr

print(square())

def tri():
    a = float(input("Въведете страна а на триъгълника:"))
    b = float(input("Въведете страна b на триъгълника:"))
    sqr = (a*b)/2
    print(sqr)



def pr():
    a = float(input("Въведете страна а на триъгълника: "))
    b = float(input("Въведете страна b на триъгълника: "))
    sqr = a*b
    print(sqr)

tri()
pr()


#2
def pol(a):
    a = list(str(a))
    b = a[::-1]
    for i in range(len(a)):
        if a[i] == b[i]:
            continue
        else:
            print(0)
            break
    else:
        print(1)

pol(12321)
pol(1234)
pol(1212344432121)

#3
f = int(input("Въведете 1, 2, 3 или 4 съответно за операция събиране, изваждане, умножение или деление: "))
a = int(input("Въведете число:"))
b = int(input("Въведете число:"))
#s 1 funkciq
def operation(f):
    if f == 1:
        result = a + b
    elif f == 2:
        result = a - b
    elif f == 3:
        result = a * b
    elif f == 4:
        result = a / b
    print(result)

operation(f)

#s nqkolko funkcii
def subirane():
    result = a+b
    print(result)

def izvajdane():
    result = a-b
    print(result)

def umnojenie():
    result = a*b
    print(result)

def delenie():
    result = a/b
    print(result)

if f == 1:
    subirane()
elif f == 2:
    izvajdane()
elif f == 3:
    umnojenie()
elif f == 4:
    delenie()
else: 
    print("Невалидно число!")
    
#4
from random import *
def f(numlist,a):
    for i in range(len(numlist)):
        if type(numlist[i]) != int:
            print("Не сте въвели списък с числа!")
            break
        numlist[i] += a + randint(0,10)
    else:
        print(numlist)

f([1,2,3],5)
f([3,4,5,2,3,1,2,3],10.5)
f("123",5)
f([2,3,"haha",2,3],14)
