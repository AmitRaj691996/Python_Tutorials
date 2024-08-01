birthdays = {
    'Sachin' : '03/14/2003',
    'Carl' : '01/17/2001',
    'Khan' :  '12/10/2006',
    'Donald' :  '06/14/2010',
    'Rohan':  '01/06/2005',
}
name = input('''Enter the person's name to get the DOB\n''')
if name in birthdays:
    print('D.O.B of '+name+' is '+birthdays.get(name))
else:
    print('Given name not found')

