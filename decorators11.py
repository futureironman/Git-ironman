'''def function():
    print("hello world")

func2=function

func2()'''
###############functin can be used to return a function#####
'''def funcret(num):
    if num==0:
        return print
    if num==1:
        return int
a=funcret(0)
#a=funcret(1)
print(a)'''


#=========we can give functin in a function as argument ===========
'''def executor(func):
    func("this")

executor(print)
'''
def dec1(func1):
    def nowexec():
        print("executing now")
        func1()
        print("Executed")
    return nowexec
@dec1#================DECORATOR===================
def who_is_sourav():
    print("Sourav is good boy.")

#who_is_sourav = dec1(who_is_sourav)
who_is_sourav()
