class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def __repr__(self):
        return 'Employee({}, {}, {})'.format(self.first, self.last, self.pay)
    def __str__(self):
        return '{} -  {}'.format(self.fullname(), self.email)
emp_1 = Employee('John', 'Smith', 10000)
emp_2 = Employee('Sue', 'Jackson', 20000)

print(emp_1)
# output : <__main__.Employee object at 0x0000013E63DB6360> which is unreadable
# when we define __repr__ now we can read what is the object


print(repr(emp_1))
print(str(emp_1))

print(emp_1.__repr__())
print(emp_1.__str__())

