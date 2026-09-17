
'''
    DICTIONARY 
    UNORDERED   no index like iterable 0, 1 but can be loop through like iterables
    but in 3.7 python it is ordered 
    MUTABLE
'''


dictionary = {
    "name": "John Doe",
    "subject": ["English", "Maths"],
    "score": 97,
    3.14: "PI"
}

print(type(dictionary))     #dict


print(dictionary[3.14])       #PI


dictionary["score"] = 95       
print(dictionary)

dictionary.keys()               #return list of keys but the type is dict_keys need to type cast it to tuple
print(dictionary.keys(),type(dictionary.keys()))     
#dict_keys(['name', 'subject', 'score', 3.14]) <class 'dict_keys'>

dictionary.values()             #returns list of values type dict_values
print(dictionary.values(),type(dictionary.values()))    
#dict_values(['John Doe', ['English', 'Maths'], 95, 'PI']) <class 'dict_values'>

dictionary.items()              #returns all the items in key value pair
print(dictionary.items(),type(dictionary.items()))     #<class 'dict_items'>
#dict_items([('name', 'John Doe'), ('subject', ['English', 'Maths']), ('score', 95), (3.14, 'PI')]) <class 'dict_items'>

# dictionary["cgpa"]               #if not found returns error 
dictionary.get("cgpa")            #returns None and executes rest of code

print("End of Code")



dictionary.update({
    "city": "Athens"
})

type_of = {"a":10,"b":20,"c":30}
print(type(type_of))
for x in type_of:
    print(x)
