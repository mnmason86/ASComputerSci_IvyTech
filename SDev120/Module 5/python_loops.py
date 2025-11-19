#This program prompts a user to enter 15 integers into a list,
#and determines whether each of those numbers is odd or even

num_list = []

for i in range(15):
    num = int(input("Enter an integer:"))
    num_list.append(num)

for num in num_list:
    if num %2 == 0:
        print(f"{num} is even")
    else: print(f"{num} is odd")

