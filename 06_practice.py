# 1. Write a Python program that takes two input numbers from the user and performs basic 
# arithmetic operations: addition, subtraction, multiplication, division, and modulus. Display 
# the results of each operation. 

# 2. Write a Python program that accepts two floating-point numbers from the user and 
# performs the same set of arithmetic operations: addition, subtraction, multiplication, division, 
# and modulus. Display the results with appropriate formatting. 

# 3. Write a Python program that takes two input numbers from the user and demonstrates the 
# use of comparison operators: equal to, not equal to, greater than, less than, greater than or 
# equal to, and less than or equal to. Display the results of each comparison. 

# 4. Write a Python program that takes three Boolean inputs from the user and demonstrates the 
# use of logical operators: and, or, and not. Display the results of each logical operation. 

a = input("enter your first : ").strip().lower() == "true"
b = input("enter your second : ").strip().lower() == "true"
c = input("enter your third : ").strip().lower() == "true"

print(f"a and b: {a and b}")
print(f"a and c: {a and c}")
print(f"b and c: {b and c}")
print(f"a not: { not a}")
print(f"(a and b ) and c: {(a and b) or c}")
print(f"a and b and c: {(a and b) and c}")

# 5. Write a Python program that takes a list and an element from the user and demonstrates the 
# use of membership operators (in, not in) and identity operators (is, is not). Display the results 
# of these operation.