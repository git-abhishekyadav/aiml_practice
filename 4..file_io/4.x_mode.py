f = open("sample2.txt","x")

f.write("new file created by x mode")

f.close()



'''
    difference between x and w mode

    w mode will truncate i.e wipe out all data and write in that file

    x mode will give error for existing file so we don't change existing file
'''


'''
    t   text mode by default binary mode
    b   (binary) audio files, video files
    +   
'''

# rt, wt, wb, rb
# r+, w+, a+

# r+        pointer at the start of the file
# w+        empty file and start of the file
# a+        pointer start at the end of the file