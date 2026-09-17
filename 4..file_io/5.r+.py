f = open("sample.txt","r+")

f.write("123")  #it read and overite the existing file with first 3 character replaced with 123
print(f.read()) # 123 was not printed because of the pointer was pointing after 123 
# but file is updated

f.close()


