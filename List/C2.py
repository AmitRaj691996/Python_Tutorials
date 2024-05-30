l=[3,5,9,8,3,4,5,9,6,3,7,2]
for i in range(len(l)-1,-1,-1):
    if l.count(l[i])>1:
        l.pop(i)
print(l)

