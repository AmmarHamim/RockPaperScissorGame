scores={'wins':0,'losses':0,'ties':0}

# def get_user_input():
#     while True:
#         user_choice = input("Rock, Paper or Scissors? (r/p/s): ").lower()
#         if user_choice in choices:
#             return user_choice
#         else:
#             print("Invalid Choice!")

# def display(user_choice,computer_choice):
#     print(f"You chose {emojis[user_choice]}")
#     print(f"Computer chose {emojis[computer_choice]}")

# def choose_winner(user_choice,computer_choice):
#     if user_choice==computer_choice:
#         print("Tie")
#         scores['ties']+=1
#     elif(
#         (user_choice== ROCK and computer_choice== SCISSORS) 
#         or (user_choice== SCISSORS and computer_choice==PAPER) 
#         or (user_choice==PAPER and computer_choice==ROCK)):
#         print("You Win 🎉 ")
#         scores['wins']+=1
#     else:
#         print("You lose 😢 ")
#         scores['losses']+=1

# def show_scoreboard():
#     print("\n📊 Scoreboard:")
#     print(f"Wins: {scores['wins']}, Losses: {scores['losses']}, Ties: {scores['ties']}\n")


# while True:

#     user_choice=get_user_input()

#     computer_choice=random.choice(choices)

#     display(user_choice,computer_choice)
#     choose_winner(user_choice,computer_choice)
    
#     should_continue=input('Wanna continue?(y/n): ').lower()
#     if should_continue=='n':
#         print("Thanks for playing! 👋")
#         show_scoreboard()
#         break