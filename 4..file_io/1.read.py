f = open("sample.txt")  #by default it is read mode

f = open("sample.txt","r")  #returns file object

data = f.read()

print(type(data), data)


data1 = f.readline()
print(data1)


f.close()


'''
    r       reading [default]
    w       writing, truncates file first -> overites
    x       creates new and open for writing
    a       writing, appends at end
    b       binary mode
    t       text mode
    +       open disk file for update (r & w)
'''