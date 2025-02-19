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
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        # instance variable which they are using Self
        # instance variables could be unique for each instance of a class
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'

    def fullname(self):
        return '{} {}'.format( self.first, self.last)

    def show_pay(Employee):
        print('Pay: {} {}'.format(Employee.pay, Employee.fullname))

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
        return "current payment of {} {} is {}".format(self.first,self.last,self.pay)


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

print(Employee.fullname(emp_1))
print(emp_1.fullname())
print(emp_1.apply_raise())


# class variables are shared among all instances of a class
# test