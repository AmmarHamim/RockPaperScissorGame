#take user input
#check validity
#let computer make a choice
#print emojis
#decide winner
# continue or not

import random
while True:
    choices = ('r','p','s')
    emojis={'r':'✊','p':'✋','s':'✌️'}

    user_choice = input("Rock, Paper or Scissors? (r/p/s): ").lower()
    if user_choice not in choices:
        print("Invalid Choice!")
        continue

    computer_choice=random.choice(choices)

    print(f"You chose {emojis[user_choice]}")
    print(f"Computer chose {emojis[computer_choice]}")

    if user_choice==computer_choice:
        print("Tie")
    elif(
        (user_choice=='r' and computer_choice=='s') 
        or (user_choice=='s' and computer_choice=='p') 
        or (user_choice=='p' and computer_choice=='r')):
        print("You Win")
    else:
        print("You lose")
    
    should_continue=input('Wanna continue?(y/n): ').lower()
    if should_continue=='n':
        break