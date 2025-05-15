# Program to demonstrate exception handling in Python

# Define a custom exception
class NegativeNumberError(Exception):
    pass

def divide_numbers():
    try:
        num1 = int(input("Enter the numerator: "))
        num2 = int(input("Enter the denominator: "))

        if num1 < 0 or num2 < 0:
            raise NegativeNumberError("Negative numbers are not allowed.")

        result = num1 / num2
        print("Result:", result)

    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")

    except ValueError:
        print("Error: Please enter valid integers.")

    except NegativeNumberError as ne:
        print("Custom Error:", ne)

    except Exception as e:
        print("An unexpected error occurred:", e)

    finally:
        print("Thank you for using the division program.")

# Call the function
divide_numbers()
