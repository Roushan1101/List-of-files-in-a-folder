import os

path = 'D:'
 
files = os.listdir(path)
for name in files:
    print(name)
a=input("\nEnter the name of the file to be searched : ")
c=0
for name in files:
    if name==a:
        c=c+1
        print(a," Is present at location : ",c)
    else:
        c=c+1
        
