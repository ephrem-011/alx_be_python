from datetime import datetime
from datetime import timedelta
def display_current_datetime():
    current_date=datetime.now()
    print (f"Current date and time: {current_date.strftime("%Y-%m-%d %H:%M:%S")}")
display_current_datetime()

def calculate_future_date(): 
    number_of_days=int(input("Enter the number of days to add to the current date: "))
    future_date=timedelta(days=number_of_days)
    print (f"Future date: {future_date.strftime}")
calculate_future_date()