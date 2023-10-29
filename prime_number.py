number=int(input("Enter the number: "))
if number==1:
    print("this is composite number")
for i in range(2,number):
    if number%i==0:
        print("This is not a prime number")
    else:
        print("This is a prime number")

    if number%i==0:
        break
    else:
        break