import datetime
import csv

# Function to display the main menu
def display_menu():
    print("\nExpense Tracker")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. View Summary")
    print("4. Exit")

# Function to add an expense
def add_expense(filename):
    try:
        date = input("Enter the date (YYYY-MM-DD): ")
        category = input("Enter the category (e.g., Food, Transport, Entertainment): ")
        amount = float(input("Enter the amount: "))
        description = input("Enter a description (optional): ")

        with open(filename, 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([date, category, amount, description])

        print("Expense added successfully!")
    except ValueError:
        print("Invalid input. Please enter a valid amount.")

# Function to view all expenses
def view_expenses(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            print("\nDate        | Category         | Amount   | Description")
            print("---------------------------------------------------")
            for row in reader:
                if len(row) == 4:
                    print(f"{row[0]:<12} {row[1]:<16} {float(row[2]):<8.2f} {row[3]}")
                else:
                    print("Invalid row format detected in file.")
    except FileNotFoundError:
        print("No expenses found. Please add an expense first.")

# Function to view summary by category
def view_summary(filename):
    try:
        summary = {}
        with open(filename, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) == 4:
                    category = row[1]
                    amount = float(row[2])
                    summary[category] = summary.get(category, 0) + amount
                else:
                    print("Invalid row format detected in file.")

        print("\nSummary by Category")
        print("Category         | Total")
        print("---------------------------")
        for category, total in summary.items():
            print(f"{category:<16} {total:<.2f}")
    except FileNotFoundError:
        print("No expenses found. Please add an expense first.")

# Main function
def main():
    filename = 'expenses.csv'

    # Ensure the CSV file has headers if it doesn't exist
    try:
        with open(filename, 'x', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Amount", "Description"])
    except FileExistsError:
        pass

    while True:
        display_menu()
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            add_expense(filename)
        elif choice == '2':
            view_expenses(filename)
        elif choice == '3':
            view_summary(filename)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
