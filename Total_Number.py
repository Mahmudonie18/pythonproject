numbers=input("Enter all the number with space: ")
numbers1=numbers.split(" ")
count=0
for i in numbers1:
    count=count+1
print(count)
for i in range(count):
    numbers1[i] = int(numbers1[i])
#print(numbers1)
maximum_number=numbers1[0]
for number in numbers1:
    if number>maximum_number:
        maximum_number=number
print(maximum_number)

