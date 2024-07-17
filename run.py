import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('expenses_calculator')


def give_date():
    """
    Function to prompt user to enter date.
    While loop to ask user to confirm data given.
    """
    print("Enter date of event.")
    print("Date should be in the format dd/mm/yyyy")

    date_input = input("Enter date here: \n")
    print(f"The date you entered is: {date_input}")
    correct_input = input("Is this correct? y/n \n")
    while True:
        if correct_input.lower() in ["yes", "y"]:
            print("Date input confirmed")
            break
        elif correct_input.lower() in ["no", "n"]:
            return give_date()
        else:
            print("Invalid input. Please re-enter correct date to continue.")
            return give_date()
    return date_input


def give_location():
    """
    Function to prompt user to insert event location.
    While loop to ask user to confirm data.
    """
    print("Please enter event location.")
    location_input = input(f"Enter event location here: \n")
    print(f"The event location you entered is: {location_input.capitalize()}")
    correct_input = input("Is this correct? y/n \n")
    while True:
        if correct_input.lower() in ["yes", "y"]:
            print("Location input confirmed")
            break
        elif correct_input.lower() in ["no", "n"]:
            return give_location()
        else:
            print("Invalid input. Please re-enter event location to continue.")
            return give_location()
    return location_input


def give_event():
    """
    Function to prompt user to insert event name.
    While loop to ask user to confirm data.
    """
    print("Please enter event type.")
    print("For example: Wedding, Funeral, etc.")
    event_input = input(f"Enter event type here: \n")
    print(f"The event type you entered is: {event_input.capitalize()}")
    correct_input = input("Is this correct? y/n \n")
    while True:
        if correct_input.lower() in ["yes", "y"]:
            print("Event input confirmed")
            break
        elif correct_input.lower() in ["no", "n"]:
            return give_event()
        else:
            print("Invalid input. Please re-enter event type to continue.")
            return give_event()
    return event_input


def give_fee():
    """
    Function to prompt user to insert fee amount.
    While loop to ask user to confirm data.
    """

    print("Please enter the fee for this event.")
    print("Fees should be in Euro (€)")
    fee_input = input(f"The fee for this event is: € \n")
    print(f"The fee you have recorded for this event is: €{fee_input}")
    correct_input = input("Is this correct? y/n \n")
    while True:
        if correct_input.lower() in ["yes", "y"]:
            print("Fee input confirmed")
            break
        elif correct_input.lower() in ["no", "n"]:
            return give_fee()
        else:
            print("Invalid input. Please re-enter correct fee to continue.")
            return give_fee()
    initial_fee = float(fee_input)
    return initial_fee


def give_travel():
    """
    Function to prompt user to insert distance travelled in kilometers.
    While loop to ask user to confirm data given.
    Convert input to float and calculate travel expenses.
    """
    print("Please enter the distance travelled for this event.")
    print("Distance should be given in kilometers")
    travel_input = input(f"The distance travelled is: (km) \n")
    print(f"You travelled {travel_input} kms for this event")
    correct_input = input("Is this correct? y/n \n")
    while True:
        if correct_input.lower() in ["yes", "y"]:
            print("Distance travelled confirmed.")
            break
        elif correct_input.lower() in ["no", "n"]:
            return give_travel
        else:
            print("Invalid input. Please re-enter distance travelled.")
            return give_travel

    travel_dist = float(travel_input)
    travel_total = travel_dist * 0.43
    print(f"Total travel expenses are €{travel_total}")
    return travel_total


def total_fee():
    """
    Function to calculate total expenses.
    Adds initial fee to travel expenses.
    Returns total amount rounded to two decimal places.
    """
    fee_total = travel_total + initial_fee
    final_fee = round(fee_total,2)
    print(f"The total fee due is €{final_fee}")
    return final_fee


def main():
    """
    Run all programme functions
    """    

give_date()
give_location()
give_event()
initial_fee = give_fee()
# give_fee()
travel_total = give_travel()
# give_travel()
total_fee()
# travel_expenses()
