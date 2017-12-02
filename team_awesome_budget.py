import csv
import datetime

def balance():
    #This opens the transactions.csv file, load everything into a list, and compare the debits and credits.
    #In the long run, this will be replaced by a database or maybe just move the file to the server...
    with open('transactions.csv','r') as csvfile:
        read_csv = csv.reader(csvfile, delimiter=',')

        transaction_list = []
        balance = 0.0
        debits = 0.0

        for row in read_csv:
            transaction_list.append(row)

        for item in transaction_list:
            if item[0] == "Debit":
                debits = debits + float(item[2])
            elif item[0] == "Credit":
                balance = balance + float(item[2])

    print(f"You have spent ${debits:.2f} of your ${balance:.2f} deposits. You have ${balance - debits:.2f} left in your account")

def update_transactions():
    #This function updates transactions.csv to keep a running tally of our debits and credits.
    #Since this is a command line application at the moment, it's just a single string.
    #Long term, I will use fields in a web interface and just commit... I hope.
    print('Enter transaction you\'d like to add\nExample "Credit,11/11/2017,1200.00,Kevin,Metro,Wedding Deposit"')
    update = input('-> ').split(',')
    with open('transactions.csv','a',newline='') as csvfile:
        write_csv = csv.writer(csvfile, delimiter=',')
        write_csv.writerow(update)

def load_budget():
    #I have another file that we use to keep note of our budget for each expenditure. This function loads that into a list
    with open('budget.csv','r') as budget_csv:
        read_csv = csv.reader(budget_csv, delimiter=',')

        budget = []

        for row in budget_csv:
            budget.append(row)

def budget_check():
    #This will take user input to get one of the categories and compare the transactions against the budget for the last
    #30, 90, 180, and 365 days.
    #Once I get it working, I'll get feedback from my wife and see what features she wants added.
    catetory = input("Which catetory do you want to check?\n-> ")

    #need to add some stuff here to do what it's supposed to do... :(
    #datetime.datetime.today().strftime('%m/%d/%Y')

while True:
    load_budget()
    #bracketted words are the input options
    selection = input("Select An Option:\n-> [Check] Balance\n-> [Update] Transactions\n-> Check [Budget]\n-> [Exit]\n-> ")

    if selection.lower() == 'check':
        balance()
    elif selection.lower() == 'update':
        update_transactions()
    elif selection.lower() == 'budget':
        pass
    elif selection.lower() == 'exit':
        print("Goodbye.")
        break
    else:
        print("You must enter a valid option")
