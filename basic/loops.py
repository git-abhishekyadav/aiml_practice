# print('Hello world')
# print('Hello world')
# print('Hello world')
# print('Hello world')
# print('Hello world')
# print('Hello world')
# print('Hello world')
# print('Hello world')
# print('Hello world')
# print('Hello world')

#what if we need to print for 1000 times
#it can be error prone 

#infinite loop
# while 3 > 2:
#     print('THis is infinite loop')

#  while 3> 2:
#     print("there a space indentation error")


# i = 1
# while i <= 10:
#     print("Hello World")
#     i +=1



'''
the loop start from 0 because of the iterator like list, starts from 0
'''


# n = int(input("Enter number"))
# i=0
# while i < 10:
#     i+=1
#     print(n * i)



'''
    break and continue in loop

    break to get out of the loop 

    continue to skip that index
'''

# n = 20
# i=0
# while i < 10:
#     i+=1
#     if i == 5:
#         break
#     if i == 3:
#         continue

#     print(i) 


#error
# n = 20
# i=0
# while i < 10:
#     if i == 5:
#         break
#     if i == 3:
#         continue              #the updation is skipped so the code is stuck in infinite loop
#     i+=1

#     print(i) 


'''
For loop -> sequential traversal
        i.e travelling in sequence one by one
'''

# word = 'hello'

#in membership operator  -> To check presence
#traversal in sequence of chararcter
# for ch in word:
#     print(ch)


#in membership operator  -> To check presence
# word = 'hello'

# if 'o' in word:
#     print('O exists')


'''
    Number of i in a word
'''

# count = 0
# word = 'artificial intelligence'
# for ch in word:
#     if 'i' in ch:
#         count+=1

# print('The count of i is', count)


'''
print vowel count
'''
# word = 'artificial intelligence'

# count = 0
# for ch in word:
#     if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
#         count += 1

# print('The count of i is', count)


# range from 0 to n-1
# range(start, stop, step)
# default range(0, n, 1)
# for i in range(5):
#     print(i)


# for i in range(1, 6):
#     print(i)


# for i in range(1,6,2):
#     print(i)

#ODD
# for i in range(1,12,2):
#     print(i)

#Even
# for i in range(0,12,2):
#     print(i)

'''
Print sum of n naturals numbers
'''

# sum = 0
# n = int(input("Enter number: "))

# for i in range(n+1):
#     # i += 1
#     sum += i

# print(sum)