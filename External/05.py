#5
# Write a program that calculates the electricity bill based on user input as
# Units consumed (int), rate per unit (float), surcharge
# ● Calculate the bill.
# ● Determine if the bill exceeds ₹500.
# ● Check eligibility for a discount.
unit = input("Enter how many unit used : ")
rate  = float(7)

bill = float(unit*rate)

print("BIll is : ",bill) + supercharge 

if bill > 500:
    print("Your bill Excced 500 rupees")
else: 
    print("your bill is under 500 reupees ")

if bill > 1000:

    discount = bill * 0.25
    final_bill = bill - discount 
    print("you are eligible for discount your discounted bill is ", final_bill)

else : 
    print("you are not eligible for discount ")
    

