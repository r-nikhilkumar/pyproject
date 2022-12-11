import os
 
#location of file
os.chdir('words')
location=os.getcwd()
location=os.getcwd()+"\words.txt"

#opening file
fo=open(location,'r')
print(fo.read())