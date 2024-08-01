dict1={
    'piece': 'portion of an object or material, produced by cutting',
    'patch': 'a piece of cloth or other material used to mend or strengthen a torn or weak point',
    'area': 'a region or a part of town, a country, or the world',
    'visit':'go to see and spend time with (someone)',
    'with': 'having or processing',
    'small': 'less than normal'
}
keys=list(dict1.keys())
values=list(dict1.values())
len=[len(x) for x in values]
print('Max',keys[len.index(max(len))])
print('Min',keys[len.index(min(len))])
