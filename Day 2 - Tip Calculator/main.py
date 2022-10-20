#DAY 2

print("Welcome to the tip calculator")
bill_total = float(input("What was the total bill? $"))
percentage_tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people_ammount = int(input("How many people will split the bill? "))
bill_with_tip = bill_total*(1+(percentage_tip/100))
each_person_pays = bill_with_tip/people_ammount  
final_ammount = round(each_person_pays, 2)
final_ammount = "{:.2f}".format(each_person_pays)

print(f"Each person should pay: ${final_ammount}")

