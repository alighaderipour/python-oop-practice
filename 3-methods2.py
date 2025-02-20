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

    @classmethod # alternative constructor
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first,last, pay)

# imagine someone is using our class and their employees are strings like below
emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

# without alternative constructor
first, last, pay = emp_str_1.split('-')
new_emp_1 = Employee(first,last, pay)

# with alternative constructor
new_emp_2 = Employee.from_string(emp_str_2)
print(new_emp_2.fullname(), new_emp_2.email)
