class Employee:
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

    def apply_raise(self):
        self.raisex = abs(self.pay - (int(self.pay * self.raise_amount)))
        self.pay = (int(self.pay * self.raise_amount))
        return "{} got {} raise".format(self.fullname(), self.raisex)



class Developer(Employee):
    pass

dev_1 = Developer("Corey", "Schafer", 50000)
dev_2 = Developer("Test", "Employee", 60000)

print(dev_1.email)
print(dev_2.email)

# method resolution order (MRO)
print('MRO')
print(help(Developer))

