
def calculator():
    while True:
        # Input numbers
        a = int(input("Enter a: "))
        b = int(input("Enter c: "))
        
        # Input operation
        c = input("Enter an operator to perform the function(+, -, *,/): ")
        
        # Perform the operation
        if c == '+':
            print(f"Sum is: {a + b}")
        elif c == '-':
            print(f"Difference is: {a - b}")
        elif c == '*':
            print(f"Product is: {a * b}")
        elif c == '/':
                print(f"n is :{a/b}")
        else:
            print("Invalid operation!")
        
        # Ask user to continue or not
        x = input("Enter 'yes', 'y' to continue or 'no', 'n' to exit: ").lower()
        if x not in ('yes', 'y','ye'):
            break

# Run the calculator
calculator()
