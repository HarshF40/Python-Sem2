import math

def calc(expression) :
    return eval(expression)

def evenOdd(number) :
    return "Even" if number % 2 == 0 else "Odd"

def factorial(number) :
    return math.factorial(int(number))

def isPrime(number) :
    number = int(number)
    if number < 2 :
        return "Composite"
    else :
        for i in range(2, number) :
            if number % i == 0 :
                return "Composite"
    return "Prime"

def main() :
    expression = input("Enter expression: ")
    result = calc(expression)
    print(result)
    print(f"The result is {evenOdd(result)}")
    print(f"Factorial of the result is {factorial(result)}")
    print(f"The result is {isPrime(result)}")

if __name__ == "__main__" :
    main()
