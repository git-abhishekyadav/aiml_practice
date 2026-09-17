'''
    search for Python from sample.txt
'''

data = True
line = 1
with open("sample.txt","r") as f:

    while data:
        data = f.readline()
        if("Python" in data):
            print(f"Python found  at line {line}")
            break

        line += 1
        
