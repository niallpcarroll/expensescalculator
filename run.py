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
    Function to prompt user to enter date. Specify date format.
    Loop to repeat if date format is invalid.
    """
   
    print("Enter date of event.")
    print("Date should be in the format dd/mm/yyyy")

    date_input = input("Enter date here: \n")
    print(f"The date you entered is {date_input}")

        

    
give_date()

