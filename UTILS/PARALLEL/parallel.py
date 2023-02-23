def add(x, y):
    """Simple function returns the sum of the arguments"""
    return x + y

def call_function(func, arg1, arg2):
    """
    Simple function that calls the function 'func' with  
    arguments 'arg1' and 'arg2', returning the result
    """
    return func(arg1, arg2)

call_function(add, 3, 7)

