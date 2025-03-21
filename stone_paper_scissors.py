import random
user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
print ("You choose")
if user_input == 0:
    print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")


elif user_input == 1:
    print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

elif user_input == 2:
    print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
else :
    print ("Wrong Input. Game Over!")

    
print ("Computer choose:")

    
computer_choice = random.randint(0,2)
if computer_choice == 0:
    print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

elif computer_choice == 1:
    print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

elif computer_choice == 2:
    print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

print ("Result:")


result = str(user_input) + str(computer_choice)

if result == "00":
    print ("It's a Draw!")
elif result == "01":
    print ("Paper beats Stone. You Lose!")
elif result == '02':
    print ("Stone beats Scissors. You Win!")
elif result == '10':
    print("Paper beats Stone. You Win!")
elif result == '11':
    print ("It's a draw!")
elif result == '12':
    print ("Scissors beats Paper! You lose!")
elif result == '20':
    print("Stone beats Scissor. You lose!")
elif result == '21':
    print("Scissor beats Paper. You win!")
elif result == '22':
    print("It's a Draw!")

play_again =input("Want to play again ? (Y/N)").lower()
if play_again == 'y':
    import stone_paper_scissors
else :
    print("Thanks For Playing!")

 
