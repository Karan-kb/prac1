#use open function to read the content of the file.

f=open('file.txt','r') #by default the mode is 'r'
data=f.read()
print(data)
f.close()