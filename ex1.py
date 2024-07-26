import math

def menu():
    print("\n Select a math function to run:")
    print("1. Square root (sqrt)")
    print("2. Factorial (factorial)")
    print("3. Greatest common divisor (gcd)")
    print("4. Sum Of Array (fsum)")
    print("5. Copy Sign (copysign)")
    print("6. Check IsNan")
    print("0. Exit")

def main():
    while True:
        menu()
        choice = int(input("Enter your choice: "))
        
        if choice == 0:
            print("Exiting the program.")
            break
        elif choice == 1:
            x = float(input("Enter a number: "))
            print("sqrt(", x, ") = ", math.sqrt(x))
        elif choice == 2:
            x = int(input("Enter a number: "))
            print("factorial(", x, ") = ", math.factorial(x))
        elif choice == 3:
            x = int(input("Enter first number: "))
            y = int(input("Enter second number: "))
            print("gcd(", x, ", ", y, ") = ", math.gcd(x, y))
        elif choice == 4:
            size = int(input("Enter the size of an array:"))
            mylist = [ int(input(f"Enter element {x+1}:")) for x in range(size)]
            print(f"fsum({mylist}):{math.fsum(mylist)}")
        elif choice == 5:
            x = float(input("Enter first parameter : "))
            y = float(input("Enter second parameter :"))
            print("copysign(", x,",",y, ") = ", math.copysign(x,y))
        elif choice == 6:
            x = math.nan
            print("IsNan(", x, ") = ", math.isnan(x))
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()