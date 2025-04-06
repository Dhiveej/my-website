s="i am Dhiveej24"
y=s.split(' ')
for i in s:
    if i.isdecimal():
        c+=1
    elif i.isalpha():
        if i.islower():
            l+=1
        else:
            l1+=1
print(c)
print(l)
print(l1)