def singleton(class_):
    instances = {}

    def get_instance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return get_instance

@singleton
class DataBase(object):

    def __init__(self):
        print("Loading Data")

db = DataBase()
db2 = DataBase()
print(db, db2)