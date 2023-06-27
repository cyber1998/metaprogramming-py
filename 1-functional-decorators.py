from functools import wraps

def logger(func):
    @wraps(func) # Copies the metadata of func into logger
    def wrapper(*args, **kwargs):
        j = 0
        for i, arg in enumerate(args):
            print(f"The {i} argument of {func.__name__}() is {arg}")
            j = i
        
        for i, arg in enumerate(kwargs):
            print(f"The {j+i} argument of {func.__name__}() is {arg}")
        return func(*args, **kwargs)
    return wrapper

@logger
def add(a, b):
    return a + b

class Person:

    def __init__(self, first_name, last_name, hobbies):
        self.first_name = first_name
        self.last_name = last_name
        self.hobbies = hobbies

    @logger
    def get_full_name(self, upper=False, a="", b="", c=""):
        full_name = f"{self.first_name} {self.last_name}"
        return full_name.upper() if upper else full_name


add(1, 2)

person = Person(first_name="Cyber", last_name="Naskar", hobbies=["Gaming", "Coding"])
person.get_full_name(upper=True, a="-", b="-", c="-")

