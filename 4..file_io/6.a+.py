f = open("sample.txt","a+")

f.write("123")  #it read and overite the existing file with first 3 character replaced with 123
print(f.read())     # nothing prints because the file pointer is at the end 

f.close()