class BmiDescriptor:

    def __get__(self, instance, owner):
        return instance.__dict__.get('__bmi', 0)

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError("Bmi can only be an integer")
        if value < 0:
            raise ValueError("Bmi cannot be less than zero")
        instance.__dict__["__bmi"] = value

    def __delete__(self, instance):
        del instance.__dict__["__bmi"]


class AgeDescriptor:

    def __get__(self, instance, owner):
        return instance.__dict__.get('__age', 0)

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError("Age can only be an integer")
        if value < 0:
            raise ValueError("Age cannot be less than zero")
        instance.__dict__["__age"] = value

    def __delete__(self, instance):
        del instance.__dict__["__age"]


class Person:
    age = AgeDescriptor()
    bmi = BmiDescriptor()

    def __init__(self, name, age, bmi):
        self.name = name
        self.age = age
        self.bmi = bmi

    def __str__(self):
        return (f"{self.name} is {self.age} years old and has Bmi of {self.bmi}")


if __name__ == "__main__":
    John = Person("John", 38, "efgesf")
    Jack = Person("Jack", 40, 28)
    print(John)
    print(Jack)
