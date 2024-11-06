import logging
import sys

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

class Person:

    def __init__(self, name):
        self._name = name


    def get_name(self):
        logging.info("getting the name")
        return self._name

    def set_name(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        logging.info("setting the name to: {}".format(name))
        self._name = name.capitalize()

    def del_name(self):
        logging.info("removing name")
        del self._name

    name = property(fget=get_name, fset=set_name, fdel=del_name)


if __name__ == "__main__":
    person1 = Person("Carl")
    print(person1.name)
    del person1.name