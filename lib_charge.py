from datetime import datetime

def calculate_fine(book_id, due_date, return_date):
    # Convert due_date and return_date strings to datetime objects
    due_date = datetime.strptime(due_date, "%Y-%m-%d")
    return_date = datetime.strptime(return_date, "%Y-%m-%d")
    
    # Calculate the number of days overdue
    days_overdue = (return_date - due_date).days
    
    # Determine the fine rate based on the number of days overdue
    if days_overdue <= 7:
        fine_rate = 20
    elif 8 <= days_overdue <= 14:
        fine_rate = 50
    else:
        fine_rate = 100
    
    # Calculate the fine amount
    fine_amount = days_overdue * fine_rate
    
    # Display the book information and fine details
    print("Book ID:", book_id)
    print("Due Date:", due_date.strftime("%Y-%m-%d"))
    print("Return Date:", return_date.strftime("%Y-%m-%d"))
    print("Days Overdue:", days_overdue)
    print("Fine Rate:", fine_rate, "shillings")
    print("Fine Amount:", fine_amount, "shillings")

# Get inputs from the user
book_id = input("Enter Book ID: ")
due_date = input("Enter Due Date (YYYY-MM-DD): ")
return_date = input("Enter Return Date (YYYY-MM-DD): ")

# Calculate and display the fine
calculate_fine(book_id, due_date, return_date)
