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
    While loop to ask user to confirm data given
    """
   
    print("Enter date of event.")
    print("Date should be in the format dd/mm/yyyy")

    date_input = input("Enter date here: \n")
    print(f"The date you entered is: {date_input}")
    correct_input = input("Is this correct? y/n \n")
    while True:
        if correct_input.lower() in ["yes", "y"]:
            print("Adding date to spreadsheet...")
            break
        elif correct_input.lower() in ["no", "n"]: 
            return give_date()  
        else:
            print("Invalid input. Please re-enter correct date to continue.")
            return give_date()
        
          
  
def give_location():
    """
    Function to prompt user to insert event location.
    """
    print("Please enter event location.")
    location_input = input(f"Enter event location here: \n")
    print(f"The event location you entered is: {location_input.capitalize()}")
    correct_input = input("Is this correct? y/n \n")
    while True:
        if correct_input.lower() in ["yes", "y"]:
            print("Adding location to spreadsheet...")
            break
        elif correct_input.lower() in ["no", "n"]: 
            return give_location()  
        else:
            print("Invalid input. Please re-enter event location to continue.")
            return give_location()

def give_event():
    """
    Function to prompt user to insert event name.
    """  
    print("Please enter event type.")  
    print("For example: Wedding, Funeral, etc.")
    event_input = input(f"Enter event type here: \n")
    print(f"The event type you entered is: {event_input.capitalize()}")

def give_fee():
    """
    Function to prompt user to insert fee amount.
    """    
    print("Please enter the fee for this event.")
    print("Fees should be in Euro (€)")
    fee_input = input(f"The fee for this event is: € \n")
    print(f"The fee you have recorded for this event is: €{fee_input}")

def give_travel():
    """
    Function to prompt user to insert distance travelled in kilometers.
    """    
    print("Please enter the distance travelled for this event.")
    print("Distance should be given in kilometers")
    travel_input = input(f"The distance travelled is: (km) \n")
    print(f"You travelled {travel_input} kms for this event")

def travel_expenses():
    """
    Function to calculate travel expenses based on distance travelled.
    """
    travel_expenses = [int(give_travel)] * 0.43
    print(travel_expenses)    
    
give_date()
give_location()
give_event()
give_fee()
give_travel()
travel_expenses()

