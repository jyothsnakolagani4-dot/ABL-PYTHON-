"""
Case Study 6: Password Policy Validation Engine
Checks passwords against length, character-category, repetition,
and prohibited-substring rules.
"""

print("PASSWORD POLICY VALIDATION ENGINE")
print("----------------------------------")

# These are the rules used in this case study.
MIN_LENGTH = 8
PROHIBITED_SUBSTRINGS = ["password", "admin", "1234"]


def validate_password(password):
    """Return a list of policy rules that the password fails."""
    failures = []

    if len(password) < MIN_LENGTH:
        failures.append("Minimum length: at least 8 characters")

    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    for character in password:
        if character.isupper():
            has_upper = True
        elif character.islower():
            has_lower = True
        elif character.isdigit():
            has_digit = True
        else:
            has_special = True

    if not has_upper:
        failures.append("Character category: include an uppercase letter")
    if not has_lower:
        failures.append("Character category: include a lowercase letter")
    if not has_digit:
        failures.append("Character category: include a digit")
    if not has_special:
        failures.append("Character category: include a special character")

    # Reject three or more identical characters in a row.
    repeated = False
    for index in range(len(password) - 2):
        if password[index] == password[index + 1] == password[index + 2]:
            repeated = True
            break

    if repeated:
        failures.append("Repetition: do not use the same character 3 times in a row")

    # Check prohibited words without considering letter case.
    lower_password = password.lower()
    for word in PROHIBITED_SUBSTRINGS:
        if word in lower_password:
            failures.append("Prohibited substring: do not include '" + word + "'")
    
    return failures


while True:
    try:
        count = int(input("How many passwords do you want to check? "))
        if count > 0:
            break
        print("Enter a number greater than zero.")
    except ValueError:
        print("Invalid input. Enter a whole number.")

for number in range(1, count + 1):
    password = input("\nEnter password " + str(number) + ": ")
    failed_rules = validate_password(password)

    print("Result:")
    if len(failed_rules) == 0:
        print("VALID - Password satisfies all policy rules.")
    else:
        print("INVALID - Password does not satisfy the policy.")
        print("Failed conditions:")
        for rule in failed_rules:
            print("- " + rule)

print("\nPassword checking completed.")
