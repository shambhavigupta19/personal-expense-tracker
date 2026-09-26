def get_non_empty_input(message):   #Get non-empty input from the user.

    while True:
        value = input(message)

        if value != "":
            return value
        else:
            print("Input cannot be empty.")

def get_positive_amount(message):   #Get a positive numeric amount from the user.
    while True:
        try:
            amount = float(input(message))

            if amount > 0:
                return amount
            else:
                print("Amount must be greater than 0.")

        except:
            print("Please enter a valid amount.")