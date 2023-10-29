age=int(input("what is your age: "))
Bill=0
if age>8:
    print("you can ride")
    #Take_photo=input("Take photos (Y/N)? ")
    if age<12:
        print("You have to pay 150Tk.")
        Bill=150
    elif age<18:
        print("You have to pay 250Tk.")
        Bill= 250
    else:
        print("you have to pay 350 Tk.")
        Bill= 350
    Take_photo = input("Take photos (Y/N)? ")
    if Take_photo== 'Y' or Take_photo== 'y':
        bill=Bill+50
        print(f"Your amount is {bill}")
    else:
        print(f"You have to pay {Bill}")

else:
    print("You can't ride")

print("Thank You")