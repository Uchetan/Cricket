'''Created to Save the Match Results
    used database is mysql
    '''

import random as rd
import mysql.connector as con
from logger import logs
import datetime
obj=[]
def first (pas='password',data_name='cricket'):
    '''Created Initialse the DataBase
    By Creating a DataBase and A table
    '''
    try:
        mydb = con.connect(host='localhost', user='root', passwd=f'{pas}', use_pure=True)
        query=f'create database {data_name}'
        cur = mydb.cursor()
        cur.execute(query)
        mydb.commit()
        mydb = con.connect(host='localhost', database= f'{data_name}',user='root', passwd=f'{pas}', use_pure=True)
        query = "create table matchistory(id int(6),team1 varchar(10),team2 varchar(10),team1_score varchar(15),team2_score varchar(15),winner varchar(10),date varchar(25));"
        cur = mydb.cursor()
        cur.execute(query)
        mydb.commit()
        obj.append(mydb)
        logs.lg.info('first time database stored sucessfully')
    except Exception as e:
        logs.lg.error('error occured at database : '+str(e))

def prep(mydb):
    query="select id from matchistory;"
    cur=mydb.cursor()
    a=cur.execute(query)
    op=[]
    for i in cur.fetchall():
        op.append(i[0])
    while True:
        b=rd.randint(10000,100000)
        if b in op:
            continue
        else:
            op.append(b)
            logs.lg.info('the id for the match was : '+str(b))
            break
    return b

def store(fir_bat,sec_bat,a1,b1,winner,pas):
    try:
        dd=str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        mydb = con.connect(host='localhost', database='cricket', user='root', passwd=f'{pas}', use_pure=True)
        data='cricket'
        b=prep(mydb)
        query=f" insert into matchistory values({b},'{fir_bat}','{sec_bat}','{a1}','{b1}','{winner}','{dd}')"
        cur = mydb.cursor()
        a = cur.execute(query)
        mydb.commit()
        logs.lg.info('data stored in database sucessfully in database : '+data)
    except Exception as e:
        logs.lg.error('error occured at database : '+str(e))
