Verify modules documentation
 (python3 -c 'print(__import__("my_module").__doc__)')

Verify classes documentation
 (python3 -c 'print(__import__("my_module").MyClass.__doc__)')

Verify functions (inside and outside a class) should have a documentation 
(python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')