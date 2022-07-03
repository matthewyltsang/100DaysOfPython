print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? $"))
percentage = (
    int(input("What percentage tip would you like to give? 10, 12, or 15? ")) / 100
)
people = int(input("How many people to split the bill? "))

per_person = round((total_bill * (1 + percentage)) / people, 2)

print(f"Each person should pay: {per_person}")
