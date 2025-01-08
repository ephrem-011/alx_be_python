def perform_operation(num1, num2, operation):
        if (operation=="add") :
            return num1+num2
        elif (operation=="subtract"):
            return num1-num2
        elif (operation=="multiply"):
            return num1*num2
        elif (operation=="divide"):
<<<<<<< HEAD
            if num2==0:
                return "Division by zero not possible"
=======
            if num2 == 0:
                print("Division by zero iss not possible")
>>>>>>> main
            else:
                return num1/num2