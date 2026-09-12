



'''
sum = a+b === operations

    Operators +

    operands  are variable a and b
'''


#arithmetic operator
a = 10
b = 5
print(a+b)
print(a-b)

print(a/b)
print(a*b)
print(a**b)
print(a%b)  #modulo


#relational or comparison operator
print(a < b)
print(a <= b)
print(a > b)
print(a >= b)
print(a != b)
print(a == b) 
#returns bool True or False

#assignment operator 
print( a = 20, b+=5, "-=")

#logical operator 
print((5 > 8) and (5 > 8))
# T and T -> T
# T and F -> F
# F and T -> F
# F and F -> F


print(not (5 > 8))
# !T -> F
print((5 > 8) or (5 > 8))
# T and T -> T
# T and F -> T
# F and T -> T
# F and F -> F

'''
#Operator precedence
()
**
* /  %
+ -
== != > >= < <=
not 
and 
or


5 * 6 / 2
if same precedence then left to right
'''

# Type Conversion
# 1. implicit conversion  > auto by python
float + int -> float
print( 5 > 9)   #converted to bool

# 2. casting 
print(int(5 + 10.0))
print(int("123"))
print(bool(10))   # every non zero is True

# compatible
# int -> float
# float -> int
# int -> bool


# int → float	✅	float(5) → 5.0	Explicit
# float → int	✅	int(5.8) → 5	Explicit
# int → bool	✅	bool(5) → True	Explicit
# str → int	✅*	int("5") → 5	Explicit
# str → float	✅*	float("5.5") → 5.5	Explicit
# str → bool	✅	bool("5") → True	Explicit



# user input

a = input("please enter a number a: ")
b = input("please enter a number b: ")

sum = a + b  # here the string concatenation 

# to fix it 
# type cast 
# but only accept int not decimal input 
sum = int(a) + int(b)

# a = int(input("please enter a number: "))



'''
PROGRAM TO CALCULATE AVG
'''

# a = int(input("please enter a number a: "))
# b = int(input("please enter a number b: "))
# avg = (a+b)/2
# print(f"Your average is {avg}")