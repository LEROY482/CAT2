#a) Polymorphism-polymorphism refers to a programming language's ability to process objects differently depending on their data type or class. More specifically, it is the ability to redefine methods for derived classes.

#b) Inheitance-It is a mechanism where you can to derive a class from another class for a hierarchy of classes that share a set of attributes and methods.

#c) Abstraction-It is selecting data from a larger pool to show only the relevant details to the object. It helps to reduce programming complexity and effort.

#d) Encapsulation-It describes the idea of bundling data and methods that work on that data within one unit.

#e) Function-It is a combination of instructions that are combined to achieve some result. A function is independent and not associated with a class

#Python program to calculate compound interest A=P(1+R/100)t

import math

Amount = float(input("Enter the amount : "))
Rate = float(input("Enter Rate of interest : "))
Time = float(input("Enter Time in years : "))
ci_future = Amount * (math.pow((1 + Rate/100), Time))
compound_int =ci_future - Amount
print ("compound interest  {0}= {1}". format(Amount, compound_int))