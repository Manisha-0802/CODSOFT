def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    if y==0:
        return "Error!Divsion by zero is not allowed."
    else:
        return x/y
def main():
    print("~~~~SIMPLE CALCULATOR~~~~")
    
    print("Select Operations:")
    print("Press '1' for Addition")
    print("Press '2' for Subtraction")
    print("Press '3' for Multiplication")
    print("Press '4' for Division")
    #Take input from the user
    choice = input("Enter your choice(1/2/3/4): ")
    # Check if choice is one of the option
    if choice in ['1','2','3','4']:
        try:
            num1=int(input("Enter the first number:"))
            num2=int(input("Enter the second number:"))
        except ValueError:
            print("Invalid input.Please enter a number:")
            return
        if choice == '1':
            print(f"The result is: {add(num1,num2)}")
        elif choice == '2':
            print(f"The result is: {subtract(num1,num2)}")
        elif choice == '3':
            print(f"The result is: {multiply(num1,num2)}")
        elif choice == '4':
            print(f"The result is: {divide(num1,num2)}")
    else:
        print("Invalid Input")

if __name__ == "__main__":
    main()
            
                     
