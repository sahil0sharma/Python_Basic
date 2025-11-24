# ----1 
# Write a program that accepts a student's marks in five subjects and calculates
# the total, average, and grade using conditional statements (if-elif-else).
# Grade criteria:
# ≥ 75: Distinction
# 60–74: First Class
# 50–59: Second Class
# 35–49: Pass

# a = int(input("Enter the marks for DMGT : "))
# b = int(input("Enter the marks for pp : "))
# c = int(input("Enter the marks for Qc : "))
# d = int(input("Enter the marks for Opps : "))
# e = int(input("Enter the marks for DSA : "))

# sum = a + b + c + d + e 

# avg = sum / 5

avg = 40

if avg >= 75:
    print("Distinction")

elif avg >= 74:
    print("first class")

elif avg >= 59:
    print("second class")

elif avg >= 49:
    print("Pass")

else :
     print("fail")
