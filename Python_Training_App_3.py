print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))


percent_total = tip / 100 * bill
sun_total = percent_total + bill
total_amount = (round(sun_total / people ,2))
print(f"Each Should Pay: $ {total_amount}")