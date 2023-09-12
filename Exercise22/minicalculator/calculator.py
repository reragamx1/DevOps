""" written calculator program to perform multiple arthmetic operation
user can select the any operation and select the display option to display the output and history stored on results.txt file"""

class Calculator:
    def __init__(self):
        self.results = []
        self.result_file = "results.txt"

    def add(self, num1, num2):
        result = num1 + num2
        self.results.append(f"Addition: {num1} + {num2} = {result}")

    def subtract(self, num1, num2):
        result = num1 - num2
        self.results.append(f"Subtraction: {num1} - {num2} = {result}")

    def multiply(self, num1, num2):
        result = num1 * num2
        self.results.append(f"Multiplication: {num1} * {num2} = {result}")

    def divide(self, num1, num2):
        if num2 != 0:
            result = num1 / num2
            self.results.append(f"Division: {num1} / {num2} = {result}")
        else:
            self.results.append("Division by zero is not allowed.")

    def display_results(self):
        for result in self.results:
            print(result)

    def save_results_to_file(self):
        with open(self.result_file, "a") as file:
            for result in self.results:
                file.write(result + "\n")

def main():
    calculator = Calculator()

    while True:
        print("\nOptions:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Display All Results")
        print("6. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            calculator.add(num1, num2)
        elif choice == "2":
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            calculator.subtract(num1, num2)
        elif choice == "3":
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            calculator.multiply(num1, num2)
        elif choice == "4":
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            calculator.divide(num1, num2)
        elif choice == "5":
            calculator.display_results()
            calculator.save_results_to_file()
        elif choice == "6":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

