# Write a python program to store the following employees data ( empcode, empname, emp salary ,
# designation ) to the sqlite database.

import sqlite3

from prettytable import PrettyTable

connection = sqlite3.connect("employee.db")

table_list = connection.execute("select name from sqlite_master where type='table' and name='employee'").fetchall()

if table_list != []:
    print("table already exsist")

else:
    connection.execute(''' create table employee(
                       Id integer primary key autoincrement,
                       empcode integer,
                       empname text,
                       emp_salary integer,
                       designation text                                        
    )''')

print("Table created!")

while True:
    print("select an option from the given menu")
    print("1. Add the  employees:")
    print("2. View all employee:")
    print("3. Exit:")

    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        getempcode = input("Enter the employee code:")
        getempname = input("Enter the employee name:")
        getempsalary = input("Enter the salary:")
        getdesignation = input("Enter the designation:")


        connection.execute(
            "insert into employee(empcode, empname, emp_salary , designation) values(" + getempcode + ", '" + getempname + "'," + getempsalary+ " ,'" + getdesignation + "')")
        connection.commit()
        print("Employee details added successfully!")

    elif choice == 2:
        result = connection.execute("select * from employee")
        table = PrettyTable(
            ["Id", "empcode", "empname", "emp_salary", "designation"])

        for i in result:
            table.add_row([i[0], i[1], i[2], i[3], i[4]])
            print(table)

    elif choice == 3:
        break

    else:
        print("invalid choice")
