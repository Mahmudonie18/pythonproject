import random
import hangman_stages
list=["orange","horse","sunflower","mango"]
chosen_word=random.choice(list)
if chosen_word=="orange" or chosen_word=="mango":
    print("Fruit Name")
elif chosen_word== "horse":
    print("Animal Name")
elif chosen_word== "sunflower":
    print("Flower name")
display=[]
lives=0
for i in chosen_word:
    display+='_'
print(display)
Game_over=False
while not Game_over:
    Guessed_leter = input("Guess The Letter: ").lower()
    for position in range(len(chosen_word)):
        letter= chosen_word[position]
        if letter==Guessed_leter:
            display[position]= Guessed_leter
    print(display)
    if Guessed_leter  not in chosen_word:
        lives+=1
        if lives==6:
            Game_over = True
            print("You Lose")
    if "_" not in display:
        Game_over = True
        print("You Win")
    print(hangman_stages.hangman_stages[lives])






