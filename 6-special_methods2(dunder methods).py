print(3 + 4)
print(int.__add__(3, 4))

print('a' + 'b')
print(str.__add__('a', 'b'))

print(len('test'))
print('test'.__len__())

class Employee:
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay

    def __add__(self, other):
        return "your total payment is {}".format(self.pay + other.pay)

    # if you comment __add__ dunder method, you get error since you cannot add two instances

    def __len__(self):
        return len(self.name)+1000

emp_1 = Employee('John', 100)
emp_2 = Employee('Sue', 200)

print(emp_1 + emp_2)

print(len(emp_1))

