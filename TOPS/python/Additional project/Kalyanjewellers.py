
#Step 1 input
name=input("Enter your name")
gender=input("Enter gender (M/F):".upper())
age=int(input("Enter your age:"))
product=input("Enter product name:")
grams=int(input("Enter product weight in grams"))
gold_price=float(input("Enter current gold price (per gram):"))

#Fixed making charges
making_charge_per_gram= 845

#Step 2: Calculation

total_gold_price= grams* gold_price

making_charge=grams* making_charge_per_gram

total_amount=total_gold_price + making_charge

#Step3 Find discount percent

discount_percent=0

if gender=="M":
    if age>65:
        if 200000 < total_amount <= 300000 :
            discount_percent=20
        elif 300000<total_amount <=500000:
            discount_percent=30
        elif total_amount>500000:
            discount_percent=35
    else:
        if 200000 < total_amount <= 300000 :
            discount_percent=10
        elif 300000<total_amount <=500000:
            discount_percent=20
        elif total_amount>500000:
            discount_percent=25

elif gender=="F":
    if age<65:
        if 200000 < total_amount <= 300000 :
            discount_percent=25
        elif 300000<total_amount <=500000:
            discount_percent=35
        elif total_amount>500000:
            discount_percent=40
    else:
        if 200000 < total_amount <= 300000 :
            discount_percent=15
        elif 300000<total_amount <=500000:
            discount_percent=25
        elif total_amount>500000:
            discount_percent=30


# step 4: Net amount

discount_amount=(total_gold_price*discount_percent/100)  


net_amount = total_amount - discount_amount

# Step 5: Print Bill
print("\n===== KALYAN JEWELLERS BILL =====")
print("Customer Name:", name)
print("Gender:", gender)
print("Age:", age)
print("Product:", product)
print("Weight (grams):", grams)
print("Gold Price per gram:", gold_price)
print("Total Gold Price:", total_gold_price)
print("Making Charges:", making_charge)
print("Total Amount (before discount):", total_amount)
print("Discount Percentage:", discount_percent, "%")
print("Discount Amount:", discount_amount)
print("Net Amount to Pay:", net_amount)
print("================================")





