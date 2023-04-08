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
SHEET = GSPREAD_CLIENT.open('love_sandwiches')

# sales = SHEET.worksheet('sales')
# data = sales.get_all_values()
# print(data)
# per the walkthrough video delete these lines of codes used to check the API was working 

# our first function : to collect the sales data from the user 

def get_sales_data():
    """
    Get sales figures input from the user
    """
    print("Please enter sales data from the last market.")
    print("Data should be six numbers, separated by commas.")
    print("Example: 10,20,30,40,50,60\n")

    data_str = input("Enter your data here:")
    print(f"The data you provided is {data_str}")

get_sales_data()

# code used below to checl API was working
# sales = SHEET.worksheet('sales')
# data = sales.get_all_values()
# print(data)


def get_sales_data():
    """
    Get sales figures input from the user
    """
# A Python function description goes between triple double quotes like this,  
# and should always be inside the function,  right underneath the function name. 

    print("Please enter sales data from the last market")
    print("Data should be six numbersm separated by a comma")
    print("Example: 10,20,30,40,50,60!")

    

# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
