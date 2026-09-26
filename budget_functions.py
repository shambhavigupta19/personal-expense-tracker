from utility_functions import get_positive_amount
def set_budget(expenses):   #Set the monthly budget and display the current budget status.

    amount = get_positive_amount("Enter your monthly budget: ₹")
    budget = amount
    total = 0

    for i in expenses:
        total = total + i[1]
    remaining = budget - total

    print("\n========== BUDGET ==========")

    print("Budget:", budget)
    print("Total Spent:", total)

    if remaining >= 0:
        print("Remaining:", remaining)
        print("You are within your budget.")
    else:
        print("Exceeded By:", abs(remaining))
        print("You have exceeded your budget.")

    print("============================")

    return budget
