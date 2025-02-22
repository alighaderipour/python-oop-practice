class Employee:
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        # instance variable which they are using Self
        # instance variables could be unique for each instance of a class
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'
        self.raisex = 0

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay += abs(self.pay - (int(self.pay * self.raise_amount)))
        return self.pay


class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, programming_language):
        super().__init__(first,last,pay)
        # it's ok to write code below aswell
        # Employee.__init__(self, first, last, pay)
        self.programming_language = programming_language


dev_1 = Developer("Corey", "Schafer", 50000, 'python')
dev_2 = Developer("Test", "Employee", 60000, 'java script')
print(dev_1.programming_language)
