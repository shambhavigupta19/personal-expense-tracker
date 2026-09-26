from utility_functions import get_non_empty_input, get_positive_amount
def add_expense(expenses):   #Add a new expense to the expense list.
    name = get_non_empty_input("Enter expense name: ")   
    amount = get_positive_amount("Enter amount: ")
    category = get_non_empty_input("Enter category: ")
    date = get_non_empty_input("Enter date: ")
    expense = [name, amount, category, date]
    expenses.append(expense)
    print("Expense added successfully!")

def view_expenses(expenses):   #Display all recorded expenses.
    if len(expenses) == 0:
        print("No expenses found.")
    else:
        print("\nYour Expenses:")
        print("----------------------------")
        for i in range(len(expenses)):
            print("Expense", i + 1)
            print("Name:", expenses[i][0])
            print("Amount: ₹", expenses[i][1])
            print("Category:", expenses[i][2])
            print("Date:", expenses[i][3])
            print("----------------------------")

def search_expense(expenses):   #Search for expenses by category.
    search = input("Enter category to search: ")
    found = False
    for i in expenses:
        if i[2].lower() == search.lower():
            print("\nName:", i[0])
            print("Amount: ₹", i[1])
            print("Category:", i[2])
            print("Date:", i[3])
            print("----------------------------")
            found = True
    if found == False:
        print("No expense found in this category.")

def delete_expense(expenses):   #Delete an expense selected by the user.   
    if len(expenses) == 0:
        print("No expenses to delete.")
    else:
        for i in range(len(expenses)):
            print(i + 1, ".", expenses[i][0], "- ₹", expenses[i][1])
        try:
            delete = int(input("Enter expense number to delete: "))
        except:
            print("Please enter a valid expense number.")
            return
        if delete >= 1 and delete <= len(expenses):
            expenses.pop(delete - 1)
            print("Expense deleted successfully!")
        else:
            print("Invalid expense number.")
