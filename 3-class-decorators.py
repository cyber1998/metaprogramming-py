from functools import wraps


def required(cls):
    original_setattr = cls.__setattr__
    def __setattr__(self, name, value):
        print(name, value)
        if value == None:
            return "Value cannot be none"
        return original_setattr(self, name, value)
    cls.__setattr__ = __setattr__  
    return cls


class RequiredFields(type):
    def __new__(cls, clsname, bases, clsdict):
        class_object = super().__new__(cls, clsname, bases, clsdict)
        class_object = required(class_object)
        return class_object

@required
class BaseEntity:

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

@required
class Employee(BaseEntity):
    pass

@required
class Employer(BaseEntity):
    pass

cyber = Employee(1, "Cyber", None)
# print(cyber.department)
