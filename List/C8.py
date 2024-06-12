L1=[[1,2,3,4], [1,2,3,4], [1,2,3,4]] 
L2=[[5,6,7,8], [5,6,7,8], [1,1,1,1]]
L3=[]
temp=[]
for i in range(len(L1)):
    for j in range(len(L1[i])):
        temp.append(L1[i][j]+L2[i][j])
    L3.append(temp)
    temp=[]
print(L3)