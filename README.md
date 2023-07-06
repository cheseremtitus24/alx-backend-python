# alx-backend-python
ALX Python

Callables
Functions, as well as lambdas, methods and classes, are represented by typing.Callable. The types of the arguments and the return value are usually also represented.
 For instance, Callable[[A1, A2, A3], Rt] represents a function with three arguments with types A1, A2, and A3, respectively. The return type of the function is Rt.

 # do_twice.py

from typing import Callable

def do_twice(func: Callable[[str], str], argument: str) -> None:
    print(func(argument))
    print(func(argument))

def create_greeting(name: str) -> str:
    return f"Hello {name}"

do_twice(create_greeting, "Jekyll")

--> Run in bash:
$ python do_twice.php
//output: 
Hello Jekyll
Hello Jekyll


Callable[..., ReturnType] (literal ellipsis) can be used to type hint a callable taking any number of arguments and returning ReturnType

from typing import Callable
# above import is deprecated in python 3.11  & you should use:
# from collections.abc import Callable
