# 1. Take inputs from the user and convert strings to numbers
bill_amount = float(input("Enter the total bill amount: $"))
tip_percentage = float(input("Enter tip percentage (e.g., 15, 18, 20): "))

# 2. Calculate tip and total amounts
tip_amount = bill_amount * (tip_percentage / 100)
total_bill = bill_amount + tip_amount

# 3. Print the results (formatted to 2 decimal places)
print("\n--- Summary ---")
print(f"Tip Amount:      ${tip_amount:.2f}")
print(f"Total Amount:    ${total_bill:.2f}") 