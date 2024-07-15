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
    print(f"The date you entered is {date_input}")

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
  

    
give_date()

