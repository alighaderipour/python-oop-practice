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

    @staticmethod
    def is_workday(day):
        if day.weekday() ==5 or day.weekday() ==6:
            return True
        return False



# if your method does not work with instance or class, then it's a static method
# instance methods work with self, class methods work with class, but static methods they don't get self/cls
# so static methods are kind of a regular method except they have some relation with our class


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

import datetime

my_date = datetime.date(2016, 7, 13)
print(Employee.is_workday(my_date))