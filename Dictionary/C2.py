dict1={
    'piece': 'portion of an object or material, produced by cutting',
    'patch': 'a piece of cloth or other material used to mend or strengthen a torn or weak point',
    'area': 'a region or a part of town, a country, or the world',
    'visit':'go to see and spend time with (someone)',
    'with': 'having or processing',
    'small': 'less than normal'
}
values_list=dict1.values()
L1=list(values_list)

l1=[]
for item in values_list:
    l1.append(len(item))
print(L1[l1.index(max(l1))])
#print(values_list[l1.index(max(l1))])
for keys_l in dict1:
    if dict1[keys_l]==L1[l1.index(max(l1))]:
        print('Longest_key:',keys_l)
for keys_s in dict1:
    if dict1[keys_s]==L1[l1.index(min(l1))]:
        print('Longest_key:',keys_s)
