'''
Q.4- Write a Python program to combine each line from first file with the corresponding line in second file.
'''

f1=open('file4_1.txt','r')
f2=open('file4_2.txt','r')

data1=f1.read()
data2=f2.read()

print("Content of file 1:\n{}".format(data1))
print("\nContent of file 2:\n{}".format(data2))

f1.seek(0)
f2.seek(0)



t1= f1.read().splitlines()
t2= f2.read().splitlines()

l1=len(t1)
l2=len(t2)

l=0
if l1>=l2:
    l=l1
else:
    l=l2
    
print("\nCOMBINED LINES ARE AS FOLLOWS:\n")

k=0
for i in range(l):
    if i<l1 and i<l2:
        print(t1[i]+" "+t2[i])
    elif i>=l1 and i<=l2:
        print(t2[i])
    elif i<=l1 and i>=l2:
        print(t1[i])


f1.close()
f2.close()

    

    
