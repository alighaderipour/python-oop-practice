class Employee:
    raise_amount = 1.04
    number_of_employees = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'
        self.raisex=0
        Employee.number_of_employees += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount 



emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

print("number of employees are : {}".format(Employee.number_of_employees))

# regular methods in a class automatically take the instance as the first argument and by convention we were calling this "self"
# how can we change this so that instead that automatically takes class as the first arguemnt? ==>> we use class methods
# we use a decorator at top of the class @classmethod

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

print('set raise amount for class')
Employee.set_raise_amt(1.05)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)