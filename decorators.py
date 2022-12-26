from functools import wraps
# Decorators

# High Order Functions
# Do at least one of the following
# - take one or more functions as arguments
# - return a function as a result


def add_three(number):
    return number + 3


def add_ten(number):
    return number + 10


def addition(add_func, number):
    return add_func(number)


# print(addition(add_three, 11))
# print(addition(add_ten, 11))

# Inner functions
# Nested functions i.e. functions defined in functions

def devision(dividend, divisor):

    def do_division():
        return dividend / divisor

    def oh_crap_zero():
        return "Oh crap zero"

    if divisor == 0:
        return oh_crap_zero

    return do_division


func_1 = devision(40, 8)
func_2 = devision(13, 0)

# print(devision(40, 8)())
# print(devision(13, 0)())
# print(func_1())
# print(func_2())


def simple_decorator(function):
    def wrapper():
        print("I am calling your function")
        function()
        print("I just called it")

    return wrapper


def say_something_dumb():
    print("Rabbits eat dog food")


# simple_decorator(say_something_dumb)()

@simple_decorator
def say_something_smart():
    print("Subscribe")


# say_something_smart()

def validate_division(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        dividend, divisor = args

        if divisor == 0:
            return "Can't divide by zero"

        return function(*args, **kwargs)
    return wrapper


@validate_division
def division(dividend, divisor):
    return dividend / divisor


# print(division(40, 8))
# print(division(30, 0))

# print(division.__name__)  # division


def repeat(amount):
    def decorator(function):
        def wrapper(*args, **kwargs):
            for i in range(amount):
                function(*args, **kwargs)
        return wrapper
    return decorator


@repeat(amount=3)
def say_something():
    print("I am being repeated")


say_something()
