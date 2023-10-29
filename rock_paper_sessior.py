import random
user_choice=int(input("Enter your turn (Rock(0)/Paper(1)/scissors(2): "))
computer_choice=random.randint(0,2)
print("computer_choice: ")
print(computer_choice)
if user_choice == computer_choice:
    print("Match drawn")
elif user_choice==2 and computer_choice==0:
    print("You Lose")
elif computer_choice ==2 and user_choice == 0:
    print("You Won")
elif user_choice < computer_choice:
    print("You Lose")
elif computer_choice < user_choice:
    print("You Won")



