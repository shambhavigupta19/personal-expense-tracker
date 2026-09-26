from datetime import datetime


def spending_report(expenses, budget):   #Generate a spending report with expense and budget details."""
    if len(expenses) == 0:
        print("No expenses available.")
        return

    total = 0
    highest = expenses[0]

    for i in expenses:
        total = total + i[1]

        if i[1] > highest[1]:
            highest = i

    average = total / len(expenses)

    dates = []

    for i in expenses:
        date = datetime.strptime(i[3], "%d-%m-%Y")
        dates.append(date)

    start_date = min(dates).strftime("%d-%m-%Y")
    end_date = max(dates).strftime("%d-%m-%Y")

    print("\n========== SPENDING REPORT ==========")
    print("Total Expenses:", len(expenses))
    print("Total Spent: ₹", total)
    print("Average Expense: ₹", average)
    print("Highest Expense:", highest[0], "- ₹", highest[1])
    print("Category:", highest[2])
    print("Report Period:", start_date, "to", end_date)

    if budget > 0:
        remaining = budget - total

        print("\nBudget Information:")
        print("Monthly Budget: ₹", budget)

        if remaining >= 0:
            print("Remaining Budget: ₹", remaining)
        else:
            print("Budget Exceeded By: ₹", abs(remaining))

    print("\nCategory-wise Spending:")

    categories = []

    for i in expenses:
        if i[2] not in categories:
            categories.append(i[2])

    for category in categories:
        category_total = 0

        for i in expenses:
            if i[2].lower() == category.lower():
                category_total = category_total + i[1]

        print(category, ": ₹", category_total)

    print("=====================================")