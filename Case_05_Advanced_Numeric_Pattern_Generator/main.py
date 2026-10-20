"""
Case Study 5: Advanced Numeric Pattern Generator
Let the user choose a filled symmetric diamond or a hollow diamond.
"""

print("ADVANCED NUMERIC PATTERN GENERATOR")
print("----------------------------------")
print("1. Symmetric filled diamond")
print("2. Hollow diamond")

while True:
    choice = input("Choose a pattern (1 or 2): ").strip()
    if choice in ("1", "2"):
        break
    print("Invalid choice. Please enter 1 or 2.")

while True:
    try:
        size = int(input("Enter diamond size (1-9): "))
        if 1 <= size <= 9:
            break
        print("Invalid size. Enter a number from 1 to 9.")
    except ValueError:
        print("Invalid input. Please enter a whole number.")

print()

# Generate the upper half, including the middle row.
for row in range(1, size + 1):
    print(" " * (size - row), end="")

    if choice == "1":
        # Filled symmetric diamond: print ascending then descending numbers.
        for number in range(1, row + 1):
            print(number, end="")
        for number in range(row - 1, 0, -1):
            print(number, end="")
        print()
    else:
        # Hollow diamond: print only the edges of each row.
        if row == 1:
            print(row)
        else:
            print(str(row) + " " * (2 * row - 3) + str(row))

# Generate the lower half, excluding the middle row.
for row in range(size - 1, 0, -1):
    print(" " * (size - row), end="")

    if choice == "1":
        for number in range(1, row + 1):
            print(number, end="")
        for number in range(row - 1, 0, -1):
            print(number, end="")
        print()
    else:
        if row == 1:
            print(row)
        else:
            print(str(row) + " " * (2 * row - 3) + str(row))

if choice == "1":
    print("Filled symmetric diamond generated successfully.")
else:
    print("Hollow diamond generated successfully.")
