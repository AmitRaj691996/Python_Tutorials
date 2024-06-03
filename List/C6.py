L1=['A','B','C','D','E','A','B','E','B','D','B','E']
result=[]
for i in range(len(L1)):
    count= L1.count(L1[i])
    if L1[i] not in result:  #take care of this Logic if not in to remove the duplicates 
        result.append(L1[i])
        result.append(count)
else:                         # else suite for>>'for'>>loop   
    print('for loop executed successfully')
    
print(result)

s='karan'
print(s.count('a'))