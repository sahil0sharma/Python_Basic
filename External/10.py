#-------10
#   Write recursive function to  
# a) Calculate factorial of a number 
# b) Generate Fibonacci series

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
n = int(input("Enter a number factorial : "))
print("factorial :",factorial(n))

def fibonacci(n):
    if n <= 1:
        return n
    else :
        return fibonacci(n-1) + fibonacci(n-2) 
    
n = int(input("Enter a number : "))
for i in range (n):
    print(fibonacci(i),end=" ")
