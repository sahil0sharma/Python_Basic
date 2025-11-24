#  ----------9
#  Write a function to print a symmetric pyramid pattern of numbers. 
# Example (for n = 4):  
# 1   
# 1 2   
# 1 2 3   
# 1 2 3 4   
# 1 2 3   
# 1 2   
# 1 

def pattern(n):
    for i in range (1, n + 1):
        for j in range (1, i + 1):
            print(j, end=" ")
        print()

    for i in range (n - 1, 0 , -1):
        for j in range (1, i + 1):
            print(j, end=" ")
        print()

n1 = int(input("Enter the no of rows : "))
pattern(n1)
