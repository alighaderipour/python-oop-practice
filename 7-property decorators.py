class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
       return self.first + '.' + self.last + '@gmail.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('John', 'Smith')
print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname())

emp_1.first = 'Jimmy'
print('chanting first name to jimmy')
print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname())

# we changed the name but it did not get updated for "email"

#test