# Open and Read mode Just open and read the content of file
f=open("sumit1.txt")
print("Content of sumit1.txt file:",f.read())

# It will write my content in file sumit2.txt and remove whatever was written
# open file in write mode write the content and close the file 
f2=open("sumit2.txt","w")
f2.write("Hey I am from Karachi")
f2.close()

# add the additional content in sumit1.txt
# it will open the file in append mode then additional text will be added and previous one will be no removed.
f=open("sumit1.txt","a")
f.write("\nStudent at DSU")
f.close()
f=open("sumit1.txt")
print("Content of sumit1.txt file:",f.read())
