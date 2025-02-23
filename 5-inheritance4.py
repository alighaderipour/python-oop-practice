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


class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, programming_language):
        super().__init__(first, last, pay)
        # it's ok to write code below too
        # Employee.__init__(self, first, last, pay)
        self.programming_language = programming_language


class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        if not self.employees:
            print('there is no employees')
        else:
            for emp in self.employees:
                print(emp.fullname())


mgr_1 = Manager('John', 'Smith', 50000)
emp_1 = Employee('John', 'Smith', 50000)
emp_2 = Employee('Sue', 'Jordan', 80000)
dev_1 = Developer('Karim', 'Jackson', 30000, programming_language='Python')

mgr_1.add_emp(emp_1)
mgr_1.add_emp(emp_2)
mgr_1.add_emp(dev_1)

mgr_1.print_emps()

print('removing Karim Jackson')

mgr_1.remove_emp(dev_1)
mgr_1.print_emps()