# Personal Expense Tracker

## Project Overview

Personal Expense Tracker is a command-line Python application that helps users record and manage their daily expenses and monitor their monthly budget.

The application allows users to add, view, search, and delete expenses. It also provides a spending report containing total spending, average expense, highest expense, budget information, and category-wise spending.

The project is developed using basic Python programming concepts and is organized into separate Python modules.

## Features

### Expense Management

- Add Expense
- View Expenses
- Search Expense by category
- Delete Expense

### Budget Management

- Set Monthly Budget
- Check budget status
- Calculate remaining or exceeded budget

### Spending Report

- Total number of expenses
- Total amount spent
- Average expense
- Highest expense
- Category-wise spending
- Budget comparison

### Category Management

- View available expense categories

## Technologies Used

- Python 3
- Visual Studio Code
- Git
- GitHub

No additional packages are required.

## Project Structure

The project contains the following files:

| File | Purpose |
|---|---|
| `main.py` | Main program and menu |
| `expense_functions.py` | Add, view, search, and delete expenses |
| `budget_functions.py` | Set and check the budget |
| `report_functions.py` | Generate the spending report |
| `category_functions.py` | Display available expense categories |
| `utility_functions.py` | Input validation and helper functions |
| `README.md` | Project documentation |
| `statement.md` | Project statement |

## File Description

### main.py

Contains the main menu and controls the overall flow of the application.

### expense_functions.py

Contains functions for adding, viewing, searching, and deleting expenses.

### budget_functions.py

Contains the function for setting the monthly budget and checking the current budget status.

### report_functions.py

Contains the function for calculating and displaying the spending report.

### category_functions.py

Contains the function for displaying the available expense categories.

### utility_functions.py

Contains helper functions for input validation, including checking for non-empty input and valid positive amounts.

## Requirements

- Python 3.x
- VS Code or any Python-supported code editor
- Command-line terminal

No additional packages are required.

## How to Run

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Open the project folder

```bash
cd personal-expense-tracker
```

### 3. Run the program

```bash
python main.py
```

If `python` does not work on your system, use:

```bash
python3 main.py
```

## How to Use

After running the program, the following menu is displayed:

```text
1. Add Expense
2. View Expenses
3. Search Expense
4. Delete Expense
5. Set Budget
6. Spending Report
7. View Categories
8. Exit
```

Enter the number of the operation you want to perform.

## Example

```text
Enter your choice: 1

Enter expense name: Lunch
Enter amount: 200
Enter category: Food
Enter date: 23-09-2026

Expense added successfully!
```

## Input Validation

The application handles common invalid inputs, including:

- Negative or zero expense amounts
- Negative or zero budget
- Invalid menu choices
- Invalid numeric input
- Empty expense names
- Empty categories
- Empty dates
- Invalid expense numbers during deletion

## Data Storage

The current version stores expense data in memory while the program is running.

The expense data is stored in a Python list and is not permanently saved after the program is closed.

## Limitations

- Expense data is not permanently stored.
- The application does not use a database or external storage.
- The application is operated through the command-line interface.

## Future Enhancements

Possible future improvements include:

- Permanent data storage using file handling
- Editing existing expenses
- Monthly and yearly reports
- Date-based expense filtering
- Graphical spending charts
- More detailed financial analysis

## Testing

To test the application, run the program using python main.py and perform each operation from the main menu using valid and invalid inputs.

The following test cases were performed:

| Test Case | Expected Result |
|---|---|
| Add a valid expense | Expense is added successfully |
| Enter an empty expense name | Error message is displayed |
| Enter an invalid amount | Error message is displayed |
| Enter a negative amount | Error message is displayed |
| View expenses | All recorded expenses are displayed |
| Search by category | Matching expenses are displayed |
| Delete a valid expense | Selected expense is deleted |
| Enter an invalid expense number | Error message is displayed |
| Set a valid budget | Budget is set successfully |
| Enter an invalid budget | Error message is displayed |
| Generate spending report | Spending statistics are displayed |
| View categories | Available categories are displayed |

## Author

**Name:** Shambhavi Gupta

**Course:** Python Essentials

**Project:** Personal Expense Tracker
