from typing import Optional
import numpy as np

# TODO: make all functions work with strings as well
# TODO: add a new cool calculator function

def sum(a: NumberOrString, b: NumberOrString) -> NumberOrString:
    '''
    Returns the sum (or concatenation) of two inputs.

    Works with:
    - numbers (int, float)
    - strings (concatenation)
    - numpy arrays (element-wise addition)
    '''
    if isinstance(a, str) and isinstance(b, str):
        return a + b
    elif isinstance(a, np.ndarray) and isinstance(b, np.ndarray):
        return np.add(a, b)
    else:
        return a + b

def multiply(a, b) -> float:
    '''
    This function returns the product of two numbers

    Args:
    a: float the first number
    b: float the second number

    Returns:
    float
    '''
    return a * b

def divide(a: float, b: float) -> float:
    '''
    ...

    Args:
    a: float the number to be divided
    b: float the divisor

    Returns:
    float
    '''
    return a / b

def modulo(a: int, b: int) -> int:
    '''
    ...

    Args:
    a: int the number to be divided
    b: int the divisor

    Returns:
    int
    '''

    return a%b

def element_wise_multiply(a: np.array, b: np.array) -> np.array:
    '''
    ...

    Args:
    a: np.array
    b: np.array

    Returns:
    np.array

    Raises:
    ValueError: if the shapes of the input arrays don't match
    '''
    if a.shape != b.shape:
        raise ValueError(f"Arrays must have the same shape. Got shapes {a.shape} and {b.shape}")

    return np.multiply(a, b)

# change output type of return_hexadecimal function
def return_hexadecimal(a: int) -> str:
    '''
    ...

    Args:
    a: float
    b: float

    Returns:
    float
    '''

    return hex(a)


def return_random_number() -> int:
    '''
    ...

    Args:
    a: float
    b: float

    Returns:
    float
    '''

    return np.random.randint(0, 100)
