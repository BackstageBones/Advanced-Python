class Singleton(type):
    instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.instances:
            cls.instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls.instances[cls]


class DataBase(metaclass=Singleton):

    def __init__(self):
        print('Loading database')


d1 = DataBase()
d2 = DataBase()
print(d1 == d2)
