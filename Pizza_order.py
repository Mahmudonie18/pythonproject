a=input("which size of pizza you need (Use must be capital letter S/M/L)? ")
if a== 'S':
    print("You will pay 100Tk.")
    Bill=100
    peperoni=input("Do you need pepperoni in small pizza (Y/N): ")
    if peperoni== 'Y' or peperoni=='y':
        bil=Bill+30
        print(f"You have to pay {bil}")
        Cheez=input("Do you need extra cheez (Y/N)? ")
        if Cheez=='Y' or Cheez=='y':
            bill=bil+20
            print(f"you have to pay {bill}")
        else:
            print(f"you have too pay {bil}")
    else:
        print(f"You have to pay {Bill}")


elif a=='M':
    print("you will pay 200Tk.")
    Bill=200
    peperoni = input("Do you need pepperoni in Medium pizza (Y/N): ")
    if peperoni == 'Y' or peperoni == 'y':
        bil = Bill + 50
        print(f"You have to pay {bil}")
        Cheez = input("Do you need extra cheez (Y/N)? ")
        if Cheez == 'Y' or Cheez == 'y':
            bill = bil + 20
            print(f"you have to pay {bill}")
        else:
            print(f"you have too pay {bil}")
    else:
        print(f"You have to pay {Bill}")

else:
    print("you will pay 300Tk.")
    Bill=300
    peperoni = input("Do you need pepperoni in Large pizza (Y/N): ")
    if peperoni == 'Y' or peperoni == 'y':
        bil = Bill + 50
        print(f"You have to pay {bil}")
        Cheez = input("Do you need extra cheez (Y/N)? ")
        if Cheez == 'Y' or Cheez == 'y':
            bill = bil + 20
            print(f"you have to pay {bill}")
        else:
            print(f"you have too pay {bil}")
    else:
        print(f"You have to pay {Bill}")

print("Thank you so much")

