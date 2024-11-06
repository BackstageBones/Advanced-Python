import time


class Lazy:

    def __init__(self, function):
        self.function = function
        self.name = function.__name__

    def __get__(self, instance, owner):
        instance.__dict__[self.name] = self.function(instance)
        # store the result of function as instances dict value
        # return it when asked again for it
        return instance.__dict__[self.name]


class Waiting:

    @Lazy
    def wait(self):
        time.sleep(3)
        return "something happened"


class EvenNumber:

    def __set_name__(self, owner, name):
        self.private_name = "__" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.private_name)

    def __set__(self, instance, value):
        setattr(instance, self.private_name, value if value % 2 == 0 else 0)


class Values:



   def __init__(self, value1, value2, value3, value4):
       self.value1 = value1
       self.value2 = value2
       self.value3 = value3
       self.value4 = value4

   value1 = EvenNumber()
   value2 = EvenNumber()
   value3 = EvenNumber()
   value4 = EvenNumber()


if __name__ == "__main__":
    wait = Waiting()
    # run 3 times and then result will be printed immediately
    print(wait.wait)
    print(wait.wait)
    print(wait.wait)
    print(wait.__dict__)
    my_values = Values(1,4,2,5)
    print(my_values.value1, my_values.value2, my_values.value3, my_values.value4)

