import pandas as pd


try:
    df = pd.read_csv("expenses.csv")
except FileNotFoundError:
    # If the file doesn't exist, create a new dataframe
    df = pd.DataFrame({"Date":[], "Category":[], "Amount":[], "Type":[]})

# Function to add a new transaction
def add_transaction():
    date = input("Enter the date (YYYY-MM-DD): ")
    category = input("Enter the expense category: ")
    amount = float(input("Enter the amount: "))
    expense_type = input("Enter the expense type (Income/Expense): ")
    
    new_row = {"Date": date, "Category": category, "Amount": amount, "Type": expense_type}
    df.loc[len(df)] = new_row
    df.to_csv("expenses.csv", index=False)
    print("Transaction added successfully!")

# Function to edit an existing transaction
def edit_transaction():
    index = int(input("Enter the index of the transaction to edit: "))
    date = input("Enter the new date (YYYY-MM-DD): ")
    category = input("Enter the new expense category: ")
    amount = float(input("Enter the new amount: "))
    expense_type = input("Enter the new expense type (Income/Expense): ")
    
    df.loc[index] = {"Date": date, "Category": category, "Amount": amount, "Type": expense_type}
    df.to_csv("expenses.csv", index=False)
    print("Transaction edited successfully!")

# Function to delete a transaction
def delete_transaction():
    index = int(input("Enter the index of the transaction to delete: "))
    df.drop(index, inplace=True)
    df.to_csv("expenses.csv", index=False)
    print("Transaction deleted successfully!")

# Function to view the expense summary
def view_summary():
    print(df)
    print("Total Expenses:", df[df["Type"] == "Expense"]["Amount"].sum())
    print("Total Income:", df[df["Type"] == "Income"]["Amount"].sum())

# Main loop
while True:
    print("""
    Personal Expense Tracker
        1. Add Transaction
        2. Edit Transaction 
        3. Delete Transaction
        4. View Summary
        5. Save and Exit
    """)
    choice = input("Enter your choice: ")
    
    if choice == "1":
        add_transaction()
    elif choice == "2":
        edit_transaction()
    elif choice == "3":
        delete_transaction()
    elif choice == "4":
        view_summary()
    elif choice == "5":
        print("Saving and exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
