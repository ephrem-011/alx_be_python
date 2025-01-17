def safe_divide(numerator, denominator):
    try:
        result=float(numerator) / float(denominator)
    except ValueError as v:
        print (v)
    except ZeroDivisionError as e:
        print (e)
    else:
        return f"The result is {result}"