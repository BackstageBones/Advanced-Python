from enum import Enum


class Address:
    def __init__(self, street, city, country):
        self.street = street
        self.city = city
        self.country = country


class AddressEnum(Enum):
    STREET = "Road street"
    CITY = "London"
    COUNTRY = "UK"


class PersonBuilder:


    def __init__(self):
        self.person = Person()
        self.lives_in()

    def called(self, name):
        self.person.name = name
        return self

    def years_old(self, age):
        self.person.age = age
        return self

    def bmi(self, bmi):
        self.person.bmi = bmi
        return self

    def lives_in(self):
        self.person.address = Address(
            AddressEnum.STREET.value,
            AddressEnum.CITY.value
            , AddressEnum.COUNTRY.value)
        return self

    def build(self):
        return self.person


class Person:

    def __init__(self):
        self.name = None
        self.age = None
        self.bmi = None
        self.address = None

    def __str__(self):
        return (f"{self.name} is {self.age} years old and has Bmi of {self.bmi},"
                f" living in {self.address.city}, {self.address.street}")

    @staticmethod
    def new():
        return PersonBuilder()


if __name__ == "__main__":
    builder = Person.new()
    John = builder.called("John") \
        .years_old(40) \
        .bmi(25).build()

    # Jack = PersonFactory.create_person("Jack", 36, 22)
    print(John)
    # print(Jack)
