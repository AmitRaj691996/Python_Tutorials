l=[3,5,9,8,3,4,5,9,6,3,7,2]
l.sort()
for i in range(0,len(l)):
    if (l.count(l[i]))>1:
        l.pop(i)
print(l)

