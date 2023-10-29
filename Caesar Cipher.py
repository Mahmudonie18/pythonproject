alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def encryption(selected_sentence,shift_step):
    chiper_text = ""
    for char in selected_sentence:
        if char in alphabet:
            position=alphabet.index(char)
            position1=(position+shift_step)%26
            chiper_text+=alphabet[position1]
        else:
            chiper_text+=char
    print(f"The final text is {chiper_text}")

def decryption(selected_sentence,shift_step):
    chiper_text_1 = ""
    for char in selected_sentence:
        if char in alphabet:
            position=alphabet.index(char)
            position1=(position-shift_step)%26
            chiper_text_1+=alphabet[position1]
        else:
            chiper_text_1+=char
    print(f"The final word is {chiper_text_1}")
wanna_end=False
while not wanna_end:
    what_to_do=input("Enter encrypt or decrypt\n")
    sentence=input("Enter the word\n")
    shift=int(input("Enter the step size\n"))
    if what_to_do=="encrypt":
        encryption(selected_sentence=sentence,shift_step=shift)
    elif what_to_do=="decrypt":
        decryption(selected_sentence=sentence,shift_step=shift)
    end=input("You want to continue?(yes or no)\n").lower()
    if end=="yes":
        wanna_end=False
    elif end=="no":
        wanna_end=True
        print("Good Bye")
