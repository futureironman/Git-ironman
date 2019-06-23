class Employee:
    no_of_leaves=8
    pass

#instances variable is the property of object

sourav=Employee()
harry=Employee()


sourav.name="sourav"
sourav.salary=765
sourav.role="Instructor"


harry.name="harry"
harry.salary=655
harry.role="student"
print(harry.name,harry.no_of_leaves)
print(harry.__dict__)#it is an attribute which return dictionary
print(Employee.__dict__)
harry.no_of_leaves=9#instance variable
print(harry.__dict__)
print(Employee.__dict__)
print(harry.no_of_leaves)