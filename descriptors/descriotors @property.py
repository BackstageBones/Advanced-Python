import logging
import sys

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

class Person:

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        logging.info("Getting name")
        return self._name

    @name.setter
    def name(self, name):
        logging.info(f"Setting the name to {name}")
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        self._name = name

    @name.deleter
    def name(self):
        logging.debug("Deleting the name")
        del self._name



if __name__ == "__main__":
    Patrick = Person("Patrick")
    print(Patrick.name)
    Patrick.name = "Paul"
    del Patrick.name
