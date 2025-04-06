a=input("ENTER A STRING:")
for i in "0123456789":
    count=0
    for ch in a:
        if ch==i:
            count +=1
    if count >0:
        print(f'the frequency of {i} is {count}')
