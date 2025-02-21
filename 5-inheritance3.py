class Employee:
    raise_amount = 1.04
   

    def __init__(self, first, last, pay):
        # instance variable which they are using Self
        # instance variables could be unique for each instance of a class
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'
        self.raisex=0
        
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay += abs(self.pay - (int(self.pay * self.raise_amount)))
        return self.pay 



class Developer(Employee):
    raise_amount= 1.10

    def __init__(self, language):
        self.language = language


emp_1 = Employee("Corey", "Schafer", 50000)
emp_2 = Employee("Test", "Employee", 60000)


dev_1 = Developer("Corey", "Schafer", 50000)
dev_2 = Developer("Test", "Employee", 60000)

print('----------------developer raise ----------------')
print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)
print('----------------employee raise ----------------')
print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

