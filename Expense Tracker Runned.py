Python 3.10.8 (tags/v3.10.8:aaaf517, Oct 11 2022, 16:50:30) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
============= RESTART: C:/Users/kudaa/Downloads/Expense Tracker.py =============

Expense Tracker
1. Add Expense
2. View Expenses
3. View Summary
4. Exit
Choose an option (1-4): 1
Enter the date (YYYY-MM-DD): 2005-11-17
Enter the category (e.g., Food, Transport, Entertainment): Transport
Enter the amount: 600
Enter a description (optional): Joburg
Expense added successfully!

Expense Tracker
1. Add Expense
2. View Expenses
3. View Summary
4. Exit
Choose an option (1-4): 1
Enter the date (YYYY-MM-DD): 2006-09-10
Enter the category (e.g., Food, Transport, Entertainment): food
Enter the amount: 500
Enter a description (optional): Snacks
Expense added successfully!

Expense Tracker
1. Add Expense
2. View Expenses
3. View Summary
4. Exit
Choose an option (1-4): 3
Traceback (most recent call last):
  File "C:/Users/kudaa/Downloads/Expense Tracker.py", line 94, in <module>
    main()
  File "C:/Users/kudaa/Downloads/Expense Tracker.py", line 86, in main
    view_summary(filename)
  File "C:/Users/kudaa/Downloads/Expense Tracker.py", line 52, in view_summary
    amount = float(row[2])
ValueError: could not convert string to float: 'Amount'
