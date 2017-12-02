import csv


def balance():
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
    print('Enter transaction you\'d like to add\nExample "Credit,11/11/2017,1200.00,Kevin,Metro,Wedding Deposit"')
    update = input('-> ').split(',')
    with open('transactions.csv','a',newline='') as csvfile:
        write_csv = csv.writer(csvfile, delimiter=',')
        write_csv.writerow(update)

def load_budget():
    with open('budget.csv','r') as budget_csv:
        read_csv = csv.reader(budget_csv, delimiter=',')

        budget = []

        for row in budget_csv:
            budget.append(row)

def budget_check():
    pass

while True:
    load_budget()
    selection = input("Select One:\n[Check] Balance\n[Update] Transactions\nCheck [Budget]\n[Exit]\n-> ")

    if selection.lower() == 'check':
        balance()
    elif selection.lower() == 'update':
        update_transactions()
    elif selection.lower() == 'budget':
        pass
    else:
        print("Goodbye.")
        break
