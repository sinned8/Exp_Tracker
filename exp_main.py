import csv
import re

# Handle user input
#   Ask user for expense name, amount, date, and possibly if its re-occuring(subscription)
#   After collecting user input, ask if there is another expense they would like to add if so repeat until not
#   once done transfer the user input to the csv file

def expenses_to_csv():

    outfile = open('expenses.csv', 'a', newline = '')
    w = csv.writer(outfile)


    while True:
        
        expense_name = input('Please enter the name of the expense: ')
       
        while True:
            try:
                amount = float(input("Please enter the dollar amount (e.g. 1.12): "))
            except ValueError:
                print("Invalid amount input...")
            else:
                break
        
        category = input('Please enter the category of the expense (e.g. food, entertainment, transportation): ')
            
        while True:
            date = input('Please enter the date of the expense in MM/DD/YYYY format: ')
            date_pattern = r"^(0[1-9]|1[0-2])/(0[1-9]|[12][0-9]|3[01])/\d{4}$"
            if re.match(date_pattern, date):
                break
            else:
                print("Invalid date input...")


        re_occuring = input('Is the expense re-occuring (y/n)? ')
        print (expense_name, amount, category, date, re_occuring)

        add_expense = input('Would you like to enter this expense (y/n)? ')

        if add_expense.lower() == 'y':
            w.writerow([expense_name, amount, category, date, re_occuring])
            print('Expense has been added...')
        elif add_expense.lower() == 'n':
            print('Expense has NOT been added...')
        else:
            print("Invalid entry, restarting...")
        
        
        expense_continue = input('Do you have another expense to add (y/n)? ')
        if expense_continue.lower() == 'y':
            return
        elif expense_continue.lower() == 'n':
            print('Aborting program...')
            exit()

    

        
        


expenses_to_csv()