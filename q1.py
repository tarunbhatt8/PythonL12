'''
Q.1- Write a Python program to read last n lines of a file
'''

f=open('file1.txt','r')
lines=f.readlines()
l=len(lines)
n=int(input("Enter the value of n: "))

if n>l:
    print("The file has only {} lines".format(len(lines)))

else:
    print("{} lines from last are as follows: ".format(n))
    for i in range(l-n,l):
        print(lines[i],end="")


f.close()
