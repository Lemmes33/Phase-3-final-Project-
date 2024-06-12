#! /usr/bin/env python3
from models.loans import *



# Test data
Bank.drop_table()
Customer.drop_table()
Loan.drop_table()

Bank.create_table()
Customer.create_table()
Loan.create_table()

Bank.create("Equity", "Nyeri")
Bank.create("Coop Bank", "Nairobi")
Bank.create("KCB Group", "Kwale")

Customer.create("Ruth", "Gathoni", "ruthyg@gmail.com", 1000000)
Customer.create("Alex", "Maranga", "alex@gmail.com", 2340000)
Customer.create("Eric", "Kirira", "eric@gmail.com", 234000)
Customer.create("Larry", "Mahiu", "larrylance@gmail.com", 45000)

Loan.create("Mortgage", 200000, 1 ,2)
Loan.create("Car-Loan", 340000, 2, 3)
Loan.create("Refinance", 160000, 3, 4)
Loan.create("Biashara", 230000, 4, 5)

Loan.create("Education-Loan", 15000, 6, 1)
Loan.create("Car-Loan", 15000, 5, 7)



# ipdb.set_trace()
