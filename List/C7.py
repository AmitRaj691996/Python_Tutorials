codes=['._', '_...', '_._.', '_..', '.', '.._.', '__.', '....', '..', '.___']
const=97
text='deface'

for x in text:
    indx = ord(x)-const
    print(codes[indx]+'\N{dollar sign}', end='')