'''
Q.3- Write a Python program to copy the contents of a file to another file
'''

import time
f1=open('file3_1.txt','r+')
f2=open('file3_2.txt','r+')

data1=f1.read()
print("Content of file 1 is:\n{}".format(data1))

data2=f2.read()
print("\nContent of file 2 is:\n{}".format(data2))

print("\nCOPYING CONTENT OF file 1 to file 2\n")

for inn in range(3):
    print('.',end="")
    time.sleep(1)
print("Copying completed")

f2.seek(0)
f2.write(data1)
f2.seek(0)
f1.seek(0)

data1=f1.read()
print("\nContent of file 1 is:\n{}".format(data1))

data2=f2.read()
print("\nContent of file 2 is:\n{}".format(data2))

f1.close()
f2.close()
