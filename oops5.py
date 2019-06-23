#==================classmethods can wen used as alternative constructor=========

class Employee:
    no_of_leaves=8
    def __init__(self,aname,asalary,arole):
        self.name=aname
        self.salary=asalary
        self.role=arole



    def printdetails(self):#here self is that instance on which the function is implemented
        return f"Name is {self.name}.Salary is {self.salary} and role is {self.role}"

    @classmethod#function can only recieve the class instance variable and change class variable
    def change_leaves(cls,newleaves):
        cls.no_of_leaves= newleaves

    @classmethod
    def from_dash(cls,string):
        return cls(*string.split("-"))
        #params=string.split("-")#it will split the string from dash
        #print(params)
        #return cls(params[0],params[1],params[2])





sourav=Employee("sourav",675,"Instructor")
harry=Employee("harry",455,"student")#if we give any argument to class then it will taken by init function
karan=Employee.from_dash("Karan-464-student")
harry.change_leaves(34)

print(karan.salary)
