from abc import ABCMeta, ABC
from enum import Enum


class VendingMachineFactory(ABC):

    def prepare(self, amount):
        pass


class HotDrink(ABC):
    def consume(self):
        pass


class Tea(HotDrink):
    def consume(self):
        print("this Tea is delicious")


class Coffee(HotDrink):

    def consume(self):
        print("this Coffee is delicious")


class HotChocolate(HotDrink):
    def consume(self):
        print("this HotChocolate is delicious")


class TeaFactory(VendingMachineFactory):

    def prepare(self, amount):
        print("Preparing tea with ", amount)
        return Tea()


class CoffeeFactory(VendingMachineFactory):

    def prepare(self, amount):
        print("Preparing coffee with ", amount)
        return Coffee()


class HotChocolateFactory(VendingMachineFactory):

    def prepare(self, amount):
        print("Preparing hot chocolate with ", amount + 'ml')
        return HotChocolate()


class UsersChoice(Enum):
    TEA = TeaFactory
    Coffee = CoffeeFactory
    HotChocolate = HotChocolateFactory


class VendingMachine:

    factories = []
    initialized = False

    def __init__(self):
        if not self.initialized:
            self.initialized = True
            for drink in UsersChoice:
                factory_name = drink.name
                factory_instance = UsersChoice[factory_name].value
                self.factories.append((drink.name, factory_instance))
            print(self.factories)


    def make_drink(self):
        print("available drinks")
        answer = input(
            f"Please choose an option: {UsersChoice.TEA.name, UsersChoice.Coffee.name, UsersChoice.HotChocolate.name}")
        amount = int(input("Specify amount: "))
        instance =  self.factories.index(answer)
        return self.factories[instance][1](amount)




if __name__ == "__main__":
    vd = VendingMachine()
    vd.make_drink()
