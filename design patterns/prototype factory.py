import copy


class Address:

    def __init__(self, street, city, suite):
        self.street = street
        self.city = city
        self.suite = suite


    def __str__(self):
        return f"{self.street}, {self.suite}, {self.city}"

class Employee(object):

    def __init__(self, name, address):
        self.name = name
        self.address = address


    def __str__(self):
        return f"{self.name} works at {self.address}"


class EmployeeFactory(object):
    main_office_employee = Employee('', Address('123 East dr', 'London' , 0))
    intern = Employee('', Address('125 East dr', 'London' , 0))

    @staticmethod
    def __new_employee(proto, name, suite):
        result = copy.deepcopy(proto)
        result.name = name
        result.address.suite = suite
        return result

    @staticmethod
    def new_office_employee(name, suite):
        return EmployeeFactory.__new_employee(
            EmployeeFactory.main_office_employee, name, suite)

    @staticmethod
    def new_intern_employee(name, suite):
        return EmployeeFactory.__new_employee(
            EmployeeFactory.intern, name, suite)

john = EmployeeFactory.new_office_employee('John', 101)
jane = EmployeeFactory.new_intern_employee('Jane', 123)
print(john)
print(jane)