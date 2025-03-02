#Write a Python program to count the number of lines in a text file.
file = open('Torezhan.txt', 'r')

cnt = 0
for _ in file:
    cnt+=1

print(cnt)