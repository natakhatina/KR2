#1
# L=[i for i in range(30,50) if i%2==1]
# for i in L: print(i)

#2
import math
#import matplotlib.pyplot as plt

# o=1 # сигма
# u=0 # мат. ожидание
#
# def res(x):
#     res=(1/(o*math.sqrt(2*math.pi)))*math.exp(-(x-u)**2/(2*o**2))
#     return res
#
# NormRasp={x:res(x) for x in range(-100,100)}
#
# for i in range(-10,11):
#     print (i,' : ',NormRasp[i])

#4
def foo(n):
    for i in range(n):
        yield (-1)**(i+1)

L=[i for i in foo(30)]
print(L)