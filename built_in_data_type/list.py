marks1 = 99
marks2 = 89
marks3 = 86

'''
    instead of creating variables to store
    we use lists


LIST is MUTABLE sequence of values
'''

# marks = [99, 89, 86, '34', 45.23]

# # print(marks[4])      invalid index

# print(len(marks) -1)  # index

# print(type(marks))


# #slicing
# print(marks[1:4])
# print(marks[:4])
# print(marks[1:len(marks)-1])
# print(marks[-5:-2])


marks = [99, 89, 86]  # no string for sort


#list methods 
#methods are classes related functions

marks.append(54)
print(marks)
marks.insert(2, 89)
print(marks)

marks.sort()
marks.sort(reverse=True)
print(marks)

marks.reverse()
print(marks)
