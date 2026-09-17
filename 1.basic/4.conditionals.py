'''
Conditional Statements
'''

# age = int(input('Please enter your age: '))
# if age >= 18: 
#     print('You can vote and drive')
# elif age <18 or age >= 13:
#     print("You are teenager can't vote and drive, study hard")
# else: 
#     print('Sorry wrong input')



# color = input('please enter the color: ')
# if color == 'red':
#     print('STOP')
# elif color == 'green':
#     print('GO')
# elif color == 'yellow':
#     print('HOLD')
# else:
#     print('WRONG INPUT')



'''
 multiple of 5 or not
'''

# n = int(input("enter number: "))
# if n % 5 == 0:
#     print("Can be divided by 5")
# else: 
#     print("Cannot divide by 5")


'''
Odd or even
'''
# a = int(input("enter number:"))
# if a % 2 == 0:
#     print("EVEN")
# else:
#     print("ODD")



#NESTED 
user='admin'
password = 'secretary'
if user == 'admin':
    if password == 'admin':
        print('Welcome admin')
    elif password == 'secretary':
        print('Welcome secretary')
    else: 
        print('Wrong password')
elif user == 'member' and password == 'member':
    print('Welcome member')
else: 
    print('Wrong Password')


color = 'yellow'
match color:
    case 'green':
        print('Go')
    case 'yellow':
        print('Hold')
    case 'red':
        print('Stop')
    case _:
        print('wrong input')