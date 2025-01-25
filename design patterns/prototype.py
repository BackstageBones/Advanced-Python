import copy


class Address:

    def __init__(self, street, city, country):
        self.street = street
        self.city = city
        self.country = country

    def __str__(self):
        return f"{self.street}, {self.city}, {self.country}"

class Person(object):

    def __init__(self, name, address):
        self.name = name
        self.address = address


    def __str__(self):
        return f"{self.name} lives at {self.address}"


class PersonFactory(object):


    @staticmethod
    def create_person(name, *args):
        return Person(name, copy.deepcopy(Address(*args)))


john = Person("John", Address("Main street", "San Francisco", "CA"))
# this uses the reference to the same class Address which is why the address of jane doesn't change
jane = john
jane.address.street = "123 London road"
print(john)
print(jane)
# this uses deepcopy inside
people_factory = PersonFactory()
john = people_factory.create_person("John", "Main street", "San Francisco", "USA")
print(john)
jane = people_factory.create_person("Jane", "123 London road", "London", "UK")
print(jane)
