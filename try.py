
from database import database
ch = input('DO YOU WANT TO STORE THE MATCH DATA (Y/N) : ')
if ch == 'y' or ch == 'Y':
    c = input('if it is your first time to store data(y/n) : -')
    if c == 'y' or c == 'Y':
        data=input()
        database.first('password',data)
        database.store('a', 'b', '88/7', '1/4', 'b','password')
    else:
        database.store('a', 'b', '88/7', '1/4', 'b','password')
else:
    print('THANKS FOR YOUR TIME')


