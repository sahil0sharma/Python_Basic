# ----7
# Write a program that displays all prime numbers between 1 and 100.

# for Number in range (1, 101):
#     count = 0
#     for i in range(2, (Number//2 + 1)):
#         if(Number % i == 0):
#             count = count + 1
#             break

#     if (count == 0 and Number != 1):
#         print(Number)


for number in range (1 , 101):
    count = 0
    for i in range(2,(number//2+1)):
        if(number % i == 0):
            count = count + 1
            break

    if(count == 0 and number !=1):
        print(number)
