#simple script for card pulls

import random

#______________________________________________

major_arc = ['the fool', 'the magician', 'the high priestess', 'the empress', 'the emperor', 'the hierophant', 
            'the lovers', 'the chariot', 'strength', 'the hermit', 'the wheel of fortune', 'justice', 'the hanged man',     
            'death', 'temperance', 'the devil', 'the tower', 'the star', 'the moon', 'the sun', 'judgement', 'the world' ]

s_values = ['ace', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'page', 'knight', 'queen', 'king']
s_names = ['cups', 'swords', 'wands', 'pentacles'] 


#new list with all suit cards    
temp = [(a, b) for a in s_values for b in s_names]
suits = [x + ' of ' + y for (x, y) in temp]


all_cards = suits + major_arc

#______________________________________________

card_pull = True

while card_pull:

    try:
        choice = input('enter value: ')
            
        for i in range(int(choice)):
            draw = str(random.choice(all_cards))
            print(draw)

        if choice == 'quit':
            card_pull = False
            
    except:
        print()
        continue

    print()



























    
