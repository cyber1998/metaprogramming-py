from exceptions import MetaException


def required(cls):
    original_setattr = cls.__setattr__

    def __setattr__(self, name, value):
        if value == None:
            raise MetaException(f'{name} cannot be None')
        return original_setattr(self, name, value)
    cls.__setattr__ = __setattr__
    return cls


class RequiredFields(type):
    def __new__(cls, clsname, bases, clsdict):
        class_object = super().__new__(cls, clsname, bases, clsdict)
        class_object = required(class_object)
        return class_object


class BaseEntity(metaclass=RequiredFields):

    def __init__(self, id, name, department):
        self.id = id,
        self.name = name
        self.department = department

# class Employee:

#     def __init__(self, id, name, department):
#         self.id = id,
#         self.name = name
#         self.department = department

# class Employer:

#     def __init__(self, id, name, department):
#         self.id = id,
#         self.name = name
#         self.department = department


class Employee(BaseEntity):
    pass


class Employer(BaseEntity):
    pass


cyber = Employee(1, "Cyber", "Computer Science")  # works
rebyc = Employee(2, "Rebyc", None)  # throws error
