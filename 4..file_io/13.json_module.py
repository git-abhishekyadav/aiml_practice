
'''

    json.loads()            s here is string        --> JSON string -> Python Obj
    json.dumps()            s represent string      --> Python obj  -> JSON strin

    json.load()              when we read from json file
    json.dump()               when we write to json file
'''

import json

json_string = '{"name":"John Doe","isTeacher":false}'

py_obj = json.loads(json_string)


print(py_obj,type(py_obj))




python_obj = {
    "name":"Siya",
    "isTeacher":False
}

json_str = json.dumps(python_obj)
print(json_str)


'''
    read from file
'''
with open("data.json", "r") as f:
    python_object = json.load(f)    #if used loads function then TypeError: the JSON object must be str, bytes or bytearray, not TextIOWrapper
    print(type(python_object))


'''
    write from file
'''

# import json

py_dict = {
    "isTeacher": False,
    "name": "Abhish"
}

with open("data2.json","w") as f:
    json.dump(py_dict, f, indent = 4, sort_keys= True)   #add indentation
    print(type(py_dict)) 