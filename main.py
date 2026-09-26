from expense_functions import add_expense, view_expenses, search_expense, delete_expense
from budget_functions import set_budget
from report_functions import spending_report
from category_functions import view_categories

print("================================")
print("    PERSONAL EXPENSE TRACKER")
print("================================")
expenses=[]
budget=0
while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Search Expense")
    print("4. Delete Expense")
    print("5. Set Budget")
    print("6. Spending Report")
    print("7. View Categories")
    print("8. Exit")

    try:
        choice = int(input("\nEnter your choice: "))
    except:
        print("Please enter a valid choice.")
        continue
    if choice == 1:
        add_expense(expenses)
    elif choice == 2:
        view_expenses(expenses)
    elif choice == 3:
        search_expense(expenses)
    elif choice == 4:
        delete_expense(expenses)
    elif choice == 5:
        budget=set_budget(expenses)
    elif choice == 6:
        spending_report(expenses, budget)
    elif choice == 7:
        view_categories(expenses)
    elif choice == 8:
        print("Thank you for using Personal Expense Tracker!")
        break
    else:
        print("Invalid choice. Please try again.")