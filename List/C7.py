codes=['._', '_...', '_._.', '_..', '.', '.._.', '__.', '....', '..', '.___']
const=97 #method to find morse_code index >>subtracting the given alphabet ASCII value from constant term to get the index in the morse code
text='deface'

for x in text:
    indx = ord(x)-const
    print(codes[indx]+' ', end='')