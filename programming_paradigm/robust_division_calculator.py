def safe_divide(numerator, denominator):
    try:
        result=numerator / denominator
    except ZeroDivisionError as e:
        print (e)
    except ValueError as v:
        print (v)
    else:
        return f"The result is {result}"