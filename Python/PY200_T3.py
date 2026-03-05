#Description: TaskPY200_T3: 
# Write program to calcite Electricity Bill Slabs. 
# User enters a bill unit and gets the total bill according to following logic. 
# Input: units Rates: • 
# First 100 @ 2/unit • 
# Next 100 (101–200) @ 3/unit • 
# Next 300 (201–500) @ 5/unit 
# • Above 500 @ 8/unit 
# Add fixed charge 50 if units > 0 Print total bill

bill_unit = int(input("Enter your Electricity bill unit: "))

if bill_unit <= 0:
    print("Enter a valid bill unit")

elif bill_unit <= 100:
    total_bill = 50 + bill_unit * 2

elif bill_unit <= 200:
    total_bill = 50 + 200 + (bill_unit - 100) * 3

elif bill_unit <= 500:
    total_bill = 50 + 200 + 300 + (bill_unit - 200) * 5

else:
    total_bill = 50 + 200 + 300 + 1500 + (bill_unit - 500) * 8


if bill_unit > 0:
    print(f"You entered electricity unit: {bill_unit}")
    print(f"Your total bill is: {total_bill}")