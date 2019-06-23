#=======self,constructor(init)======

class Employee:
    no_of_leaves=8
    def __init__(self,aname,asalary,arole):
        self.name=aname
        self.salary=asalary
        self.role=arole



    def printdetails(self):#here self is that instance on which the function is implemented
        return f"Name is {self.name}.Salary is {self.salary} and role is {self.role}"



#sourav=Employee()
harry=Employee("harry",455,"student")#if we give any argument to class then it will taken by init function

'''
sourav.name="sourav"
sourav.salary=765
sourav.role="Instructor"


harry.name="harry"
harry.salary=655
harry.role="student"
'''
print(harry.printdetails())

