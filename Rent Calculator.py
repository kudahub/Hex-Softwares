# Rent Calculator

def calculate_rent_split():
    try:
        # Input total rent amount
        total_rent = float(input("Enter the total rent amount: "))

        # Input number of roommates
        num_roommates = int(input("Enter the number of roommates (including yourself): "))

        if num_roommates <= 0:
            print("The number of roommates must be at least 1.")
            return

        # Collect additional costs
        utilities = float(input("Enter the total utility costs: "))
        other_expenses = float(input("Enter other shared expenses (e.g., internet): "))

        # Calculate total expenses
        total_expenses = total_rent + utilities + other_expenses

        # Calculate per person share
        share_per_person = total_expenses / num_roommates

        # Display results
        print("\n=== Rent Split Summary ===")
        print(f"Total Rent: ${total_rent:.2f}")
        print(f"Utilities: ${utilities:.2f}")
        print(f"Other Expenses: ${other_expenses:.2f}")
        print(f"Total Expenses: ${total_expenses:.2f}")
        print(f"Each person owes: ${share_per_person:.2f}")
    except ValueError:
        print("Invalid input. Please enter numeric values.")

# Main function to run the calculator
def main():
    while True:
        print("\n=== Rent Calculator ===")
        print("1. Calculate Rent Split")
        print("2. Exit")

        choice = input("Choose an option (1-2): ")

        if choice == '1':
            calculate_rent_split()
        elif choice == '2':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
