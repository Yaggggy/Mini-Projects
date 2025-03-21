print ("Welcome to the tip calculator")
total_bill = float (input("What was the total bill?$"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15?"))
people = int(input("How many people to split the bill?"))
tip_amount = (total_bill * tip_percentage)/100
bill_with_tip = tip_amount + total_bill
amount_to_pay = round(bill_with_tip /people,2)
print(f"Each person should pay: ${amount_to_pay}")
