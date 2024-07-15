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
    """
   
    print("Enter date of event.")
    print("Date should be in the format dd/mm/yyyy")

    date_input = input("Enter date here: \n")
    print(f"The date you entered is: {date_input}")

def validate_date(values):
    """
    Validate if date format is eight digits long.
    """
    try:
        [int(value) for value in values]
        if len(values) !=8:
            raise ValueError(
                f"Date format must be ddmmyyyy, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid date: (e), try again")
  
def give_location():
    """
    Function to prompt user to insert event location.
    """
    print("Please enter event location.")
    location_input = input(f"Enter event location here: \n")
    print(f"The event location you entered is: {location_input}")

def give_event():
    """
    Function to prompt user to insert event name.
    """  
    print("Please enter event type.")  
    print("For example: Wedding, Funeral, etc.")
    event_input = input(f"Enter event type here: \n")
    print(f"The event type you entered is: {event_input}")

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
    travel_expenses = int(travel_input) * 0.43
    print(travel_expenses)    
    
give_date()
give_location()
give_event()
give_fee()
give_travel()
travel_expenses()

