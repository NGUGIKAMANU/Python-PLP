def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount if the discount is 20% or higher.

    Parameters:
        price (float): Original price of the item.
        discount_percent (float): Discount percentage to apply.

    Returns:
        float: Final price after discount if applicable, otherwise the original price.
    """
    if discount_percent >= 20:
        # Apply discount by calculating discounted price
        return price * (1 - discount_percent / 100)
    # Return original price if discount is less than 20%
    return price

# Get and validate original price input
original_price = None
while original_price is None:
    try:
        original_price = float(input("Enter the original price of the item: "))
    except ValueError:
        print("Error: Please enter a valid number for the price (e.g., 50.99).")

# Get and validate discount percentage input
discount_percentage = None
while discount_percentage is None:
    try:
        discount_percentage = float(input("Enter the discount percentage: "))
    except ValueError:
        print("Error: Please enter a valid number for the discount (e.g., 15).")

# Calculate the final price using the function
final_price = calculate_discount(original_price, discount_percentage)

# Display results with context
if discount_percentage >= 20:
    # Format numbers to 2 decimal places for currency display
    print(f"✅ Applied a {discount_percentage:.1f}% discount. Final price: ${final_price:.2f}")
else:
    print(f"❌ No discount applied. Original price remains: ${final_price:.2f}")