food = ['pizza', 'nuggets', 'hotdog', 'noodles', 'pasta', 'burger']
#print(food[0][0]) To access first letter of food item in list food
letter=input('Please, Enter the letter!!\n')
for i in range(0,len(food)):
    if food[i].startswith(letter.upper()) or food[i].startswith(letter.lower()) :
        print(food[i], end=',')
