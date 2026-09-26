from datetime import datetime


def get_non_empty_input(message):   #Get non-empty input from the user.
    while True:
        value = input(message).strip()

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


def get_valid_date(message):   #Get a valid date from the user in DD-MM-YYYY format.
    while True:
        date = input(message).strip()

        try:
            datetime.strptime(date, "%d-%m-%Y")
            return date
        except:
            print("Please enter a valid date in DD-MM-YYYY format.")