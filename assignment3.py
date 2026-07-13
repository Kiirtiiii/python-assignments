# Assignment 3: Online Shopping Discount Calculator

customer_name = input("Enter Customer Name: ")
purchase_amount = float(input("Enter Total Purchase Amount : Rs."))
premium = input("Are you a Premium Member? (Yes/No): ")

# Calculate Discount
if purchase_amount < 2000 :
    Discount = 0
elif purchase_amount < 5000 :
    Discount = purchase_amount * 0.10
else :
    Discount = purchase_amount * 0.20

# Additional discount for premium members
if premium.lower() == "yes" :
    Discount += purchase_amount * 0.05

final_bill = purchase_amount - Discount

# Display Bill 
print("\n-----BILL-----")
print("Customer Name :", customer_name)
print("Original Bill : Rs.", purchase_amount)
print("Discount : Rs.", Discount)
print("Final Amount : Rs.", final_bill)

#Bonus
if final_bill > 10000:
    print("Eligible for Free Shipping")