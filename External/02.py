# ----2
# Write a program to input two integer values and perform all bitwise 
# operations (AND, OR, XOR, NOT, Left Shift, and Right Shift). Display the 
# binary representation of inputs and results for following numbers and 
# perform Left Shift, and Right Shift by 3 digits. 
# Number1= 43 and Number2 = 74 

num1 = 43
num2 = 74

bitwise_and = num1 and num2
bitwise_or = num1 or num2
bitwise_not1 = ~ num1
bitwise_not2 = ~ num2
bitwise_right1 = num1 >> 3
bitwise_left1 = num1 << 3
bitwise_right2 = num2 >> 3
bitwise_left2 = num2 << 3

print("And = ", bitwise_and)
print("or = ", bitwise_or)
print("Not of 43 = ", bitwise_not1)
print("Not of 74 = ", bitwise_not2)
print("Right shift 43 = ", bitwise_right1)
print("Left shift 43 = ", bitwise_left1)
print("Right shift 74 = ", bitwise_right2)
print("Left shift 74 = ", bitwise_left2)



