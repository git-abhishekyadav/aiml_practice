'''
    function blocks of statement that performs specific tasks


    definition -> logic

    call -> invoke


    reusable component of code
'''

# def fnx():                  #fnx definition
#     print('Hello WOrld')


# fnx()                       #fnx call or invoke to run the function




#input parameter 
    
#output return


# def sum(a, b): # a and b paramters
#     return a + b

# print(sum(4, 5))  # values arguments



# calc average
# def avg(a,b,c):
#     return (a+b+c)/3

# val = avg(3,4,5)
# print(val)


# first non default paramter  and at last the default parameter
# else will get error
# def sum(a,b = 1):
#     return a + b

# print(sum(4))

'''
Built in functions

range()
input()
type()
print()
'''

'''
user defined functions 
sum()
avg()
'''

'''
LAMBDA function


usage in higher order function
 those are simply function which takes function as parameter or return function
'''

sum = lambda a,b: a+b

print(sum(3,4))



'''
n factorial 
'''
n = int(input('Please enter number: '))

def fact_func(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i

    return fact

print(fact_func(n))