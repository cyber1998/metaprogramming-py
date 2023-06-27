from functools import wraps, partial

POSTFIX = "+++"
INCOMPATIBLE_DATATYPE_ERR = "{} Incompatible datatype detected: {} of type {}"
UNSUPPORTED_DATATYPE = "{} Iterables and other datastructures are not supported"

def typechecker(func=None, *, postfix=""):
    if func is None:
        return partial(typechecker, postfix=postfix)
    @wraps(func)
    def wrapper(*args, **kwargs):

        if type(args[0]) not in [float, str, int]:
            return UNSUPPORTED_DATATYPE.format(POSTFIX)
        if len(args) > 1:
            datatype = type(args[0])
        for arg in args[1:]:
            if type(arg) != datatype:
                return INCOMPATIBLE_DATATYPE_ERR.format(POSTFIX, arg, type(arg))
        return func(*args, **kwargs)
    return wrapper



@typechecker(postfix=POSTFIX)
def add(a, b):
    return a + b


# Passes
assert add(1, 2) == 3
assert add("Pro", "gramming") == "Programming"
assert add(1.5, 3.5) == 5.0

# Fails (Incompatible datatypes)
assert add(1, 2.1) == INCOMPATIBLE_DATATYPE_ERR.format(POSTFIX, 2.1, float)
assert add(2.1, 2) == INCOMPATIBLE_DATATYPE_ERR.format(POSTFIX, 2, int)
assert add(2.1, "What?") == INCOMPATIBLE_DATATYPE_ERR.format(POSTFIX, "What?", str)
assert add(1, [2]) == INCOMPATIBLE_DATATYPE_ERR.format(POSTFIX, [2], list)

# Fails (Unsupported datatypes)
assert add([1], [2]) == UNSUPPORTED_DATATYPE.format(POSTFIX)



