"""
Project 1: Age Calculator

You have to create a program that will calculate user's age.

The program will ask the user to enter their name and their DOB (date of birth) in the following format: dd/mm/yyyy

The program will then calculate the user's age based on current year (2024)

The program will also print out a message to the user with their name and age.

Optional: You can prompt for various formats of DOB like dd/mm/yy, dd-mm-yyyy, yyyy/mm/dd, yyyy-mm-dd, etc.

Example:
Input:
Enter your name: Prerna
Enter your DOB (dd/mm/yyyy): 07/07/2004

Output:
Hello Prerna! You are 20 years old.
"""

Name = input("Enter your name : ")

DOB = input("Enter your DOB (dd/mm/yyyy): ")

Current = 2024

# 0123456789
# dd/mm/yyyy
year = int(DOB[6:10])
Age = 2024 - year

print("Hello " , Name,"! you are " , Age, " years old.", sep='')


"""
Congratulations!

You've created your 1st project by yourself.

"""