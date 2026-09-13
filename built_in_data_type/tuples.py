tup = (34,36,26,12)

tup[2] = 10        # IMMUTABLE
#TypeError tuple object doesn't support item assignment

print(tup, type(tup),len(tup))


tup = (1)    #int
tup = ('abc')   #str
 
#to create single value tuple
single_tuple = (1,)        #tuple


#slicing
print(tup[:])


for val in tup:
    print(val)


sum = 0
for val in tup:
    sum+= val

print(f"the sum of tuple {sum}")


'''
    TUPLES METHOD
'''

tup = (23,12,23,234)

tup.index(23)               #return 1st occurance index ->  0

tup.count(23)                  #returns total occurances -> 2