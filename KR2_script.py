#1
L=[i for i in range(30,50) if i%2==1]
for i in L: print(i)

#2
import math

o=1 # сигма
u=0 # мат. ожидание

def res(x):
    res=(1/(o*math.sqrt(2*math.pi)))*math.exp(-(x-u)**2/(2*o**2))
    return res

NormRasp={x:res(x) for x in range(-100,100)}

for i in range(-10,11):
    print (i,' : ',NormRasp[i])
#3
for i in range(10,-11,-1):
    print (i,' : ',NormRasp[i])



#4
def foo(n):
    for i in range(n):
        yield (-1)**(i+1)

L=[i for i in foo(30)]
for i in L: print(i)

#5
import random,math

def fooSin(k):
    k=k * math.pi / 180
    yield math.sin(k)

def fooCos(k):
    k = k * math.pi / 180
    yield math.cos(k)

def foo(n):
    for i in range(n):
        k = random.randint(0, 180)
        if k % 2 == 0:
            a=fooSin(k)
            yield next(a)
        else:
            a=fooCos(k)
            yield next(a)

L=[i for i in foo(50)]
print(L)
