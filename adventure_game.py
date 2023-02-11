choice = input ('You are lost in a forest during the night. You find a FLASH LIGHT and a LIGHTER. You can only take one of them, what is your choice?  ').lower()

if choice == 'lighter':
    print ('You picked the LIGHTER')
elif choice == 'flash light':
    print ('You picked the FLASH LIGTH ')
else: 
    print("code didn't work")

choice_2 = input ('You found a cave and it is time to eat. You have two choices, a PROETIEN or a TUNA CAN, what do you pick? ').lower()

if choice_2 == 'protein bar':
    print ('You choose the protein bar!')
elif choice == 'tuna can':
    print('You choose the tuna!')

choice_3 = input ( 'You walk down the maountain where you cave was. You run into a dead end but you see that the rocks blocking the way are easy to climb, but you also see a river next to the big rock. do you CROSS the river or CLIMB the rocks?  ').lower()

if choice_3 == 'cross':
    print ('You choosed to cross!')
elif choice_3 == 'climb':
    print('You choosed climb!')

print ('You grabbed a ' + choice +'. You ate '+ choice_2 + '. You choosed to ' + choice_3)

choice_4 = input('You have crossed to the other site of the forest. You see two paths, one on the LEFT, one on the RIGHT. What path do you choose?').lower()

if choice_4 == 'rigth':
     print('You choosed to go rigth!')  
elif choice_4 == 'left':
    print ('You choosed left!')

choice_5 = input('You have found a secret door on the way. Do you OPEN it or do you WALK away?').lower()

if choice_5 == 'open':
    print ('You opened the door!')
elif choice_5 == 'walk':
    print ('You walked away from the door!')

choice_6 = input('You have been walking for around 5 hours and you see a bright light a couple meters out, you also heard the noise of cars driving around. Do you follow the LIGHT or the NOISE? ').lower()

if choice_6 == 'light':
    print('You followed the light!')
elif choice_6 == 'noise':
    print('You followed the noise!')

print (choice_4 +' you went' + choice_5 + '. you followed' + choice_6)

print ('You have make it back to the city safe! :)')







    


 

