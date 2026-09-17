'''
    WITH

    we don't need to close explicitly

    there's an possibility that someone might not close file and maybe corrupted existing one
    
'''


with open("sample.txt", "r") as f:
    data = f.read()
    print(data)
    print(len(data))