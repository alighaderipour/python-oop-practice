# Python Object-Oriented Programming
"""
class Employee:
    pass


emp_1 = Employee()
emp_2 = Employee()
print(emp_1)
print(emp_2)

# Instance Variable
emp_1.name = 'Ali'
emp_1.last = 'Ghaderi Pour'
emp_1.email = 'ali.ghaderipour@gmail.com'
emp_1.pay = 50000

emp_2.name = 'test'
emp_2.last = 'user'
emp_2.email = 'test.user@gmail.com'
emp_2.pay = 60000

print(emp_1.email)
print(emp_2.email)

"""


class Employee:
    # class variables are shared among all instances of a class
    raise_amount = 1.04
    number_of_employees = 0

    def __init__(self, first, last, pay):
        # instance variable which they are using Self
        # instance variables could be unique for each instance of a class
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'
        self.raisex=0
        Employee.number_of_employees += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def show_pay(Employee):
        return "current payment of {} {} is {}".format(Employee.first, Employee.last, Employee.pay)

    def apply_raise(self):
        self.raisex = abs(self.pay - (int(self.pay * self.raise_amount)))
        self.pay = (int(self.pay * self.raise_amount))
        return "{} got {} raise".format(self.fullname(), self.raisex)



emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

print(Employee.fullname(emp_1))
print(emp_1.fullname())
print(emp_1.apply_raise())
print(emp_1.show_pay())

print('------------------------------------------')
print(emp_1.__dict__) # there is no raise_amount attribute
print(Employee.__dict__) # the class has the attribute
print(emp_1.raise_amount) # if we don't find the attribute in instance, we look at parents
print(Employee.raise_amount)
print(emp_2.raise_amount)


print('------------------------------------------')
# now if we change the attribute value from class it gonna change for class and all instances
Employee.raise_amount = 1.05
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

print('------------------------------------------')
# but if we change class attribute from instance, it gonna change only for that instance
emp_1.raise_amount = 1.06
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

# and now we can see emp_1 raise_amount in __dict__
print(emp_1.__dict__)
print(emp_2.__dict__) # still no raise_amount

# so if we had a class attribute , we can change the value of an attribute of class without changing  value of class attribute
# or other instance attribute's value
# of that class attribute

print("number of employees are : " , Employee.number_of_employees)