l=[3,5,9,8,3,4,5,9,6,3,7,2]
l.sort()
for x in l:
    if l.count(x)>1:
        l.pop(l.index(x))
print(l)

