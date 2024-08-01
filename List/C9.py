L1=[[1,2,3,4], [1,2,3,4], [1,2,3,4]]
L2=[]
for j in range(len(L1[0])):
    temp = []
    for i in range(len(L1)):
        temp.append(L1[i][j])
    L2.append(temp)
print(L2)
