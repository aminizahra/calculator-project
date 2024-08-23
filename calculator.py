num1 = 10
num2 = 5
def add(x, y):
    return x + y

def subtract(x, y:
    return x - y

def main():
    # Manual input for testing
    num1 = 10  # Example value for the first number
    num2 = 5   # Example value for the second number

    print("Select operation:")
    print("1. Add")
    print("2. Subtract")

    choice = "1"  # Example operation selection

    if choice == '1':
        print(f"The result of adding {num1} and {num2} is: {add(num1, num2)}")
    elif choice == '2':
        print(f"The result of subtracting {num2} from {num1} is: {subtract(num1, num2)}")
    else:
        print("Invalid Input")

if __name__ == "__main__":
    main()
