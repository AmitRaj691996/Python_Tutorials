fav1=['pizza','nuggets','hotdog','noodles','pasta','burger']
fav2=['burger','hotdog','noodles','pasta','nuggets','pizza']
f=[]
n=[]
for i in range(len(fav1)):
    temp=fav1[i]
    j = fav2.index(temp)
    f.append(temp)
    n.append(i+j)
print(f,'\n',n)
indx=n.index(min(n))
print(f[indx],min(n))
print('Please have',f[indx],'as your favourite dish')