class BmiDescriptor:

    def __init__(self):
        self.__bmi = 0

    def __get__(self, instance, owner):
        return self.__bmi

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError("Bmi can only be an integer")
        if value < 0:
            raise ValueError("Bmi cannot be less than zero")

        self.__bmi = value

    def __delete__(self, instance):
        del self.__bmi


class AgeDescriptor:

    def __init__(self):
        self.__age = 0

    def __get__(self, instance, owner):
        return self.__age

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError("Age can only be an integer")
        if value < 0:
            raise ValueError("Age cannot be less than zero")

        self.__age = value

    def __delete__(self, instance):
        del self.__age


class Person:
    bmi = BmiDescriptor()
    age = AgeDescriptor()

    def __init__(self, name, age, bmi):
        self.name = name
        self.age = age
        self.bmi = bmi

    def __str__(self):
        return f"{self.name} is {self.age} years old and has Bmi of {self.bmi}"


if __name__ == "__main__":
    John = Person("John", 32, 20)
    Jack = Person("Jack", 40, 25)
    print(Jack)
    print(John)
    # Jack overrides John age
