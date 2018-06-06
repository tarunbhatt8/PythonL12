'''
Q.2- Write a Python program to count the frequency of words in a file.
'''
f=open('file2.txt','r')
lines=f.readlines()
search=input("Enter word to count frequency of: ")
fr=0

for i in lines:
    words=i.split()
    for j in words:
            if j==search:
                 fr+=1

print("The word {} occurs {} times in the file.".format(search,fr))

f.close()

