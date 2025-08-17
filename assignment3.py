def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        return price - (price * discount_percent / 100)
    else:
        return price

# Get user input
price = float(input("Enter the original price: "))
discount = float(input("Enter the discount percentage: "))

# Calculate final price
final_price = calculate_discount(price, discount)

# Print result
print("Final price:", final_price)
