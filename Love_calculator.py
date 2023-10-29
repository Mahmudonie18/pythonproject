name1=input("what is your name: ")
name2=input("what is his/her name: ")
combine_name= name1+name2

lower_case_letter=combine_name.lower()
t=combine_name.count('t')
r=combine_name.count('r')
u=combine_name.count('u')
e=combine_name.count('e')
true= t + r + u + e
l=combine_name.count('l')
o=combine_name.count('o')
v=combine_name.count('v')
e=combine_name.count('e')
love= l + o + v + e

Love_score=str(true)+str(love)
print(f"{lower_case_letter}")

print(f"Your love score is {Love_score}%")

#print("Thank you so much")