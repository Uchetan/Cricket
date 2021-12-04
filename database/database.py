import random as rd
import mysql.connector as con
from logger import logs
'''used database is mysql '''
def first (pas='password',data_name='circket'):
    try:
        mydb = con.connect(host='localhost', user='root', passwd=f'{pas}', use_pure=True)
        query=f'create database {data_name}'
        cur = mydb.cursor()
        cur.execute(query)
        mydb.commit()

        mydb = con.connect(host='localhost', database= f'{data_name}',user='root', passwd=f'{pas}', use_pure=True)
        query = "create table matchistory(id int(6),team1 varchar(10),team2 varchar(10),team1_score varchar(15),team2_score varchar(15),winner varchar(10));"
        cur = mydb.cursor()
        cur.execute(query)
        mydb.commit()
        f=open("database\\object.txt","w")
        f.write(data_name+","+pas)
        f.close()
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

def store(fir_bat,sec_bat,a1,b1,winner,):
    try:
        f=open('database\\object.txt','r')
        a = f.read()
        a = a.split(',')
        mydb = con.connect(host='localhost', database=f'{a[0]}', user='root', passwd=f'{a[1]}', use_pure=True)
        b=prep(mydb)
        query=f" insert into matchistory values({b},'{fir_bat}','{sec_bat}','{a1}','{b1}','{winner}')"
        cur = mydb.cursor()
        a = cur.execute(query)
        mydb.commit()
        logs.lg.info('data stored in database sucessfully')
    except Exception as e:
        logs.lg.error('error occured at database : '+str(e))
