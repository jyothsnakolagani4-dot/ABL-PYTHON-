"""
Case Study 4: Multi-Product Shopping Budget Constraint
Evaluates a shopping basket, applies threshold discounts, and reduces quantities
until the total fits within the shopper's budget.
"""

def calculate_bill(products):
    subtotal = sum(price * quantity for name, price, quantity in products)
    if subtotal >= 5000:
        discount_rate = 0.10
    elif subtotal >= 2500:
        discount_rate = 0.05
    else:
        discount_rate = 0.0
    discount = subtotal * discount_rate
    return subtotal, discount, subtotal - discount, discount_rate


def main():
    print("MULTI-PRODUCT SHOPPING BUDGET PLANNER")
    budget = float(input("Enter your shopping budget (Rs): "))
    while budget < 0:
        print("Budget cannot be negative.")
        budget = float(input("Enter your shopping budget (Rs): "))

    count = int(input("Enter number of different products: "))
    while count <= 0:
        print("Please enter at least one product.")
        count = int(input("Enter number of different products: "))

    products = []
    for i in range(count):
        print(f"\nProduct {i + 1}")
        name = input("Product name: ").strip()
        while not name:
            print("Product name cannot be empty.")
            name = input("Product name: ").strip()

        price = float(input("Unit price (Rs): "))
        while price < 0:
            print("Price cannot be negative.")
            price = float(input("Unit price (Rs): "))

        quantity = int(input("Quantity: "))
        while quantity < 0:
            print("Quantity cannot be negative.")
            quantity = int(input("Quantity: "))

        products.append([name, price, quantity])

    original = [item.copy() for item in products]
    original_subtotal, original_discount, original_total, original_rate = calculate_bill(products)

    print("\n--- ORIGINAL BASKET ---")
    for name, price, quantity in original:
        print(f"{name}: {quantity} x Rs {price:.2f} = Rs {price * quantity:.2f}")
    print(f"Subtotal: Rs {original_subtotal:.2f}")
    print(f"Discount rate: {original_rate * 100:.0f}%")
    print(f"Discount: Rs {original_discount:.2f}")
    print(f"Total after discount: Rs {original_total:.2f}")
    print(f"Budget: Rs {budget:.2f}")

    reductions = []
    # Reduce one unit at a time from the most expensive available product.
    while calculate_bill(products)[2] > budget:
        candidates = [item for item in products if item[2] > 0]
        if not candidates:
            break
        selected = max(candidates, key=lambda item: item[1])
        selected[2] -= 1
        reductions.append(selected[0])

    subtotal, discount, final_total, rate = calculate_bill(products)

    print("\n--- RECOMMENDED BASKET ---")
    for name, price, quantity in products:
        print(f"{name}: {quantity} x Rs {price:.2f} = Rs {price * quantity:.2f}")
    print(f"Revised subtotal: Rs {subtotal:.2f}")
    print(f"Discount rate: {rate * 100:.0f}%")
    print(f"Discount: Rs {discount:.2f}")
    print(f"Final total: Rs {final_total:.2f}")
    print(f"Money remaining: Rs {budget - final_total:.2f}")

    if reductions:
        print("\nQuantity reductions made (one unit at a time):")
        for name in reductions:
            print(f"- Removed one unit of {name}")
    else:
        print("\nYour original basket is already within budget; no reductions needed.")

    if final_total <= budget:
        print("Status: Basket fits within budget.")
    else:
        print("Status: Unable to fit the basket within budget.")


if __name__ == "__main__":
    main()
