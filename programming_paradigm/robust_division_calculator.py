def safe_divide(numerator, denominator):
    try:
        numerator=float(numerator)
        denominator=float(denominator)
        print (f"The result of the division is {numerator / denominator}")
    except ValueError:
        print( f"Error: Please enter numeric values only." )
    except ZeroDivisionError:
        print ("Error: Cannot divide by zero.")
   