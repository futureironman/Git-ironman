#--------map---------

'''number =["3","34","64"]
number=list(map(int,number))

#for i in range(len(number)):
   # number[i]=int(number[i])


number[2] =number[2]+1
#print(number[2])

#def sq(a):
   # return a*a


square=list(map(lambda x:x*x,num))
print(square)
'''
'''def square(a):
    return a*a


def cube(a):
    return a*a*a


func=[square,cube]
#num=[2,3,5,6,7,8,9]
for i in range(5):
    val =list(map(lambda x:x(i),func))
    print(val)'''




###############filter

'''list_1=[1,2,3,4,5,6,7,8,9]

def is_greater_5(num):
    return num>5

greater_than_5=list(filter(is_greater_5,list_1))
print(greater_than_5)
'''
#------------reduce---------
from functools import reduce#reduce is a part of functool module


list1=[1,2,3,4,5]
num=reduce(lambda x,y:x+y,list1)
print(num)

prod=reduce(lambda x,y:x*y,list1)
print(prod)



