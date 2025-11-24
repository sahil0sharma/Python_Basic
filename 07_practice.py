# 1. Write a Python program that takes a student's score as input and uses conditional 
# statements to determine the corresponding grade. The grading system is as follows: 
# ● Score >= 90: Grade A 
# ● Score >= 80: Grade B 
# ● Score >= 70: Grade C 
# ● Score >= 60: Grade D 
# ● Score < 60: Grade F 

# score = int(input("enter your score: "))

# if score >= 90:
#     print("Grde A ")

# elif score >= 80:
#     print("Grade B")
# elif score >= 70:
#     print("Grade C")
# elif score >= 60:
#     print("Grade D")
# elif score < 60:
#     print("Grade F")

# 2. Write a Python program that takes a positive integer n as input and uses a while loop to 
# calculate and print the sum of the first n natural numbers. 

# n = int(input("Enter the no. upto sum you want : "))

# sum = 0
# i = 1
# while n >= i:
#     sum +=i
#     i+=1
# print("sum of first ",n ,"no is ",sum)


# 3. Write a Python program that takes an integer n as input and uses a for loop to generate and 
# print the multiplication table for that number up to 10. 

# n1 = int(input("Enter the no you want multiplication of : "))

# for i in range (10):
#     mul = n1 * i
#     print(n1," * " ,i, "= ",mul)   #do with while loop
    



# 4. Write a Python program that takes a positive integer n as input and uses nested loops to 
# print a right-angled triangle pattern of n rows using asterisks (*). 

n2 = int(input("Enter the no. : "))

for i in range (n2 + 1):
    print(i * "*")

# 5. Write a Python program that implements a simple number guessing game. The program 
# should generate a random number between 1 and 100 and allow the user to guess the number. 
# The program should provide feedback if the guess is too high or too low. The game should 
# continue until the user guesses the correct number or decides to quit by entering 0. Use break 
# and continue statements to control the flow of the game. 

