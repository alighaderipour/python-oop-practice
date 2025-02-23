print(3+4)
print(int.__add__(3,4))

print('a' + 'b')
print(str.__add__('a', 'b'))


class Employee:
    def __init__(self, name, pay):
        self.name = name
        self.pay pay

emp_1 = Employee('John', 100)
