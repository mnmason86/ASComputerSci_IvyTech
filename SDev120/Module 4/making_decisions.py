
#This program takes in a user's name and final grade,
#and prints whether they passed or not based on their grade


name = str(input("Please enter your name: "))
grade = int(input("Please enter your final grade:"))

if grade >= 60:
    status = "passed"

if grade < 60:
    status = "failed"

print("Hello,", name, "you", status, "this class.")
    
    
