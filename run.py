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
    print("Welcome to your expenses calculator!")
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
    print(f"You travelled {travel_input}km for this event")
    correct_input = input("Is this correct? y/n \n")
    while True:
        if correct_input.lower() in ["yes", "y"]:
            print("Distance travelled confirmed.")
            break
        elif correct_input.lower() in ["no", "n"]:
            return give_travel()
        else:
            print("Invalid input. Please re-enter distance travelled.")
            return give_travel()
    
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

def collect_data():
    all_data = [(date_input), (location_input.capitalize()), (event_input.capitalize()), (initial_fee), (travel_total), (final_fee)]
    return all_data


def update_worksheet(all_data):
    """
    Collects data given and adds it to worksheet.
    """
    print("Adding the following data to datasheet:")
    print(f"Date: {date_input}")
    print(f"Location: {location_input}")
    print(f"Event: {event_input}")
    print(f"Fee:€{initial_fee}")
    print(f"Travel expenses: €{travel_total}")
    print(f"Total fee: €{final_fee}")
    expenses_worksheet = SHEET.worksheet("expenses")
    expenses_worksheet.append_row(all_data)
    print("Data successfully added to Google Sheet!")


def main():
    """
    Run all programme functions
    """

date_input = give_date()
location_input = give_location()
event_input = give_event()
initial_fee = give_fee()
travel_total = give_travel()
final_fee = total_fee()
all_data = collect_data()
update_worksheet(all_data)



