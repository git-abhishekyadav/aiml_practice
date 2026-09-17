squares = []

for i in range(6):
    squares.append(i*i)

print(squares)



# [output iterable condition]

square = [i*i  for i in range(6)]
print(square)


'''
    only odd
'''

odd_square = [i*i for i in range(6) if i%2!=0]
print(odd_square)


# replace -ve with 0
nums = [-1,-23,-3, 2,34,23]

output = [0 if val<0 else val for val in nums]
print(output)


#uppercase
words = ["hello","python","john","doe"]
uppercase_word = [val.upper() for val in words]
print(uppercase_word)