word = 'python'



# print(word[2])

# word[2] = 'T'     Errror string is immutable it can't be changed

# length of string
print(len(word))

# sequence of character

# for ch in word:
#     print(ch)


# slicing 
    # sub string
    # str[ starting ind: ending ind] -> where ending index is not included

# word = 'I study from YT'


# print(word[13:])

# word = 'python'
# print(word[2:4]) #th
# # forward 1 to n

# # and reverse is -n to -1
# print(word[-4:-2])



'''
    string formatting
'''
a = 10
b = 5
sum = a + b
print('the sum is {}'.format(sum))
#normal formatting
print('this language is {}'.format('python'))

print('the sum of {} and {} is {}'.format(a, b, sum))


#index formatting
print('the sum of {1} and {0} is {2}'.format(a, b, sum))


#value based formatting
print("{a} and {b}".format(a=5, b=20))


'''
    f strings
    literal string interpolation
'''

print(f"the sum of {a} and {b} is {a+b}")
