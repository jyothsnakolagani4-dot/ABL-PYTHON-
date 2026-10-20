# Case 10: Food Waste Monitoring System
# Compares meals prepared, served, and left over across several days.

print("FOOD WASTE MONITORING SYSTEM")

while True:
    try:
        days = int(input("Enter number of days to monitor: "))
        if days > 0:
            break
        print("Please enter a positive number of days.")
    except ValueError:
        print("Please enter a whole number.")

while True:
    try:
        limit = float(input("Enter acceptable wastage limit (0-100%): "))
        if 0 <= limit <= 100:
            break
        print("Limit must be between 0 and 100.")
    except ValueError:
        print("Please enter a valid number.")

day_names = []
prepared_list = []
served_list = []
leftover_list = []
wastage_list = []
consistent_list = []

for i in range(days):
    print("\nDay", i + 1)
    while True:
        name = input("Enter day name/label: ").strip()
        if name != "":
            break
        print("Day label cannot be empty.")

    while True:
        try:
            prepared = int(input("Meals prepared: "))
            served = int(input("Meals served: "))
            leftovers = int(input("Leftover meals: "))
            if prepared >= 0 and served >= 0 and leftovers >= 0:
                break
            print("Meal counts cannot be negative.")
        except ValueError:
            print("Please enter whole numbers for meal counts.")

    consistent = (prepared == served + leftovers)

    if prepared > 0:
        wastage = leftovers / prepared * 100
    else:
        wastage = None

    day_names.append(name)
    prepared_list.append(prepared)
    served_list.append(served)
    leftover_list.append(leftovers)
    wastage_list.append(wastage)
    consistent_list.append(consistent)

total_prepared = sum(prepared_list)
total_served = sum(served_list)
total_leftovers = sum(leftover_list)

print("\n========== DAILY WASTE REPORT ==========")
for i in range(days):
    print("\nDay:", day_names[i])
    print("Prepared:", prepared_list[i])
    print("Served:", served_list[i])
    print("Leftovers:", leftover_list[i])

    if wastage_list[i] is None:
        print("Wastage percentage: N/A (no meals prepared)")
    else:
        print("Wastage percentage: {:.2f}%".format(wastage_list[i]))
        if wastage_list[i] > limit:
            print("Alert: Wastage exceeds the acceptable limit.")
        else:
            print("Status: Within acceptable limit.")

    if consistent_list[i]:
        print("Meal count check: Consistent")
    else:
        print("Meal count check: MISMATCH (prepared != served + leftovers)")

print("\n========== OVERALL SUMMARY ==========")
print("Total meals prepared:", total_prepared)
print("Total meals served:", total_served)
print("Total leftover meals:", total_leftovers)

if total_prepared > 0:
    overall_wastage = total_leftovers / total_prepared * 100
    print("Overall wastage percentage: {:.2f}%".format(overall_wastage))
    if overall_wastage > limit:
        print("Overall alert: Wastage exceeds the acceptable limit.")
    else:
        print("Overall status: Within acceptable limit.")
else:
    print("Overall wastage percentage: N/A (no meals prepared)")

mismatch_count = 0
for i in range(days):
    if not consistent_list[i]:
        mismatch_count += 1

print("Days with meal-count mismatches:", mismatch_count)
print("Monitoring complete.")
