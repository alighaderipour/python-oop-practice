print(3 + 4)
print(int.__add__(3, 4))

print('a' + 'b')
print(str.__add__('a', 'b'))


class Employee:
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay

    def __add__(self, other):
        return "your total payment is {}".format(self.pay + other.pay)


emp_1 = Employee('John', 100)
emp_2 = Employee('Sue', 200)

print(emp_1 + emp_2)
