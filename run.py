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
    while True:
        print("Enter date of event.")
        print("Date should be in the format dd/mm/yyyy")

        date = input("Enter date here:\n")

        if valid_data(date):
            print("Date is correct!")
            break
    return date

def valid_data():
    """
    Check to ensure that date values are in the correct format.
    """        


def main():
    date = give_date()
print("Welcome to your travel expenses calculator! Let's calculate and record your recent expenses.")
main()

