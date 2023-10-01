# Get the charge for the food from the user
food_charge = float(input("Enter the charge for the food: $"))

# Calculate the tip
tip_percentage = 18
tip_amount = (tip_percentage / 100) * food_charge

# Calculate the sales tax
tax_percentage = 7
tax_amount = (tax_percentage / 100) * food_charge

# Calculate the total amount
total_amount = food_charge + tip_amount + tax_amount

# Display each amount and the total price
print(f"Food Charge: ${food_charge:.2f}")
print(f"Tip ({tip_percentage}%): ${tip_amount:.2f}")
print(f"Sales Tax ({tax_percentage}%): ${tax_amount:.2f}")
print(f"Total Price: ${total_amount:.2f}")
