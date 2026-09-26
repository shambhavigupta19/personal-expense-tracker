def view_categories(expenses):   #Display all unique expense categories.

    if len(expenses) == 0:
        print("No expenses available.")
        return

    categories = []

    for i in expenses:
        if i[2] not in categories:
            categories.append(i[2])

    print("\n========== CATEGORIES ==========")

    for i in range(len(categories)):
        print(i + 1, ".", categories[i])

    print("================================")