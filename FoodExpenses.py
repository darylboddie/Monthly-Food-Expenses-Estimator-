import sqlite3 
# Create a database
def init():
    conn = sqlite3.connect("spent.db")
    cur = conn.cursor()
    sql = '''
    create table if not exists expenses (
        amount number,
        category string,
        message string,
        date string
        )
    '''
    cur.execute(sql)
    conn.commit()
init()

# Track and input expense to the database
def log(amount, category, message=""):
    from datetime import datetime
    date = str(datetime.now())
    conn = sqlite3.connect("spent.db")
    cur = conn.cursor()
    sql = '''
    insert into expenses values (
         {},
        '{}',
        '{}',
        '{}'
          )
          
    '''.format(amount, category, message, date)
    try:
        cur.execute(sql)
        conn.commit()
        print('\nExpense saved!\n')
    except:
        print('\nExpense not saved. Try again')

# View expenses for month and category 
def view(date,category):
    conn = sqlite3.connect("spent.db")
    cur = conn.cursor()
    if category.isalpha():
        sql = '''
        select * from expenses where category = '{}' and date like '{}%'
        '''.format(category, date)
        sql2 = '''
        select sum(amount) from expenses where category = '{}' and date like '{}%'
        '''.format(category, date)
        cur.execute(sql)
        results = cur.fetchall()
        cur.exceute(sql2)
        total_amount = cur.fetchone()[0]

        for expense in results:
            print(expense)
        print('\nTotal:','$' + str(total_amount))

# Create introduction and instructions to explain the purpose of the code
print("\nWelcome to Monthly Food Expenses!")
print("View the total amount you have spent in a month")

# Gather user input to use different functions if the input is true
while True:
    print("1- Initialize database\n2 - Enter the amount\n3 - View monthly food expense\nQ - Quit")
    ans = input(":")
    print()

    if ans == "1":
        init()
        print('Database initialized')
    if ans == "2":
        cost = input("What is the amount spent?\n: ")
        category = input("Enter the expense category\n: ")
        msg = input("Where was the amount spent?\n: ")
        log(cost,category,msg)
    elif ans == "3":
        date = input("Enter the date (yyyy-mm)\n: ")
        category = input("Enter the category you would like to review or press enter to view all expenses\n: ").title()
        print()
        view(category,date)
    elif ans.lower() == "q":
        print("Goodbye!\n")
        break
    

    
       


