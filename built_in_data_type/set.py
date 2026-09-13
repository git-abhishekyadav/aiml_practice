'''
    SET collection of unique elements

    set itself is mutable 
    the elements are immutables data types
    UNordered
'''

s = {1,2,2,3,3,4,5}

s.add(6)

s.remove(2)
print(s)
s.pop()             #removes random or arbitrary value
print(s)

s.add((23,23,21))
# s.add({"a":10})         #Mutable element cannot be added error

print(s)
print(len(s))           #there will be no duplicate



#EMPTY SET

empty_set = {}
#this creates dictionary

empty_set = set()

# empty_set.add(2,3,4,5,5)      ERROR

print(empty_set)

s1 ={1,2,3,4}
s2 ={2,3,4,5,6}

print(s1.union(s2))
print(s1.intersection(s2))


