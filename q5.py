'''
Q.5- Write a Python program to write 10 random numbers into a file. Read the file and then sort the numbers and then store it to another file.
'''

import random
f=open('file5_1.txt','w')

print("Generating 10 random numbers and writing them in file: \n")
for i in range(10):
    num=random.randint(1,1000)
    f.write(str(num)+"\n")

f.close()

f1=open('file5_1.txt','r+')

t1= f1.read().splitlines()
print("Reading the content of file: \n")
print(t1)
      
for i in range(len(t1)):
    t1[i]=int(t1[i])

print("Sorting the numbers...\n")
t1.sort()

f2=open('file5_2.txt','w')
print("Storing the sorted numbers in an other file: ")

for i in range(len(t1)):
    f2.write(str(t1[i])+"\n")

f2.close()

f2=open('file5_2.txt','r+')
print("Reading the sorted content stored in the  other file: ")
data=f2.read()
print(data)

f.close()
f1.close()
f2.close()


    
