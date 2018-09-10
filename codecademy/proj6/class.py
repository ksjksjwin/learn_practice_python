"""
- A class is a template for a data type. It describes the kinds of information that class will hold and how a programmer will interact with that data
- A class instance is also called an object. The pattern of defining classes and creating objects to represent the responsibilities of a program is known as Object Oriented Programming or OOP.

Instantiation takes a class and turns it into an object, the type() function does the opposite of that. When called with an object, it returns the class that the object is an instance of.

print(type(cool_instance))
# prints "<class '__main__.CoolClass'>"
We then print out the type() of cool_instance and it shows us that this object is of type __main__.CoolClass.

In Python __main__ means "this current file that we're running" and so one could read the output from type() to mean "the class CoolClass that was defined here, in the script you're currently running."

- A class variable is a variable that's the same for every instance of the class.

You can define a class variable by including it in the indented part of your class definition, and you can access all of an object's class variables with object.variable syntax.
"""
