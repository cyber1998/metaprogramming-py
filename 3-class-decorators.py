from exceptions import MetaException


def required(cls):
    """
    Decorator to make sure that any of the fields are not None.
    Raises:
        MetaException: If any of the fields are None.

    Returns:
        cls: The class with the __setattr__ method overridden.
    """
    original_setattr = cls.__setattr__

    def __setattr__(self, name, value):
        if value == None:
            raise MetaException(f'{name} cannot be None')
        return original_setattr(self, name, value)
    cls.__setattr__ = __setattr__
    return cls


class RequiredFields(type):
    """
    Metaclass that inherits from type and overrides the __new__ method.
    It then returns the class with the __setattr__ method overridden.
    """
    def __new__(cls, clsname, bases, clsdict):
        class_object = super().__new__(cls, clsname, bases, clsdict)
        class_object = required(class_object)
        return class_object


class BaseEntity(metaclass=RequiredFields):
    """
    Base class that inherits from object and has the metaclass RequiredFields.
    """

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
