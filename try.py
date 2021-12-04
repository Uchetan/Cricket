trial={'a':[1,2,4,2,5,2,4,],'b':[2,5,4,8,4,2,11]}
out={1:[2,1,5,222],2:[2,5,2,6,1,4,4]}

rec=[trial,
     out]
print(rec)
def store(te_bat1,te_bat2,te_bowl1,te_bowl2,tot1,tot2):
    te_bat1['total']=tot1
    te_bat2['total']=tot2
    ins=[te_bat1,te_bat2,te_bowl1,te_bowl2]
    print(ins)

while True:
    a=rd.randint(10000,99999)
    if a in op:
        continue
    else:
        op.append(a)
        rec = {'ids': op}
        collection.drop()
        collection.insert_one(rec)
        break
def store():
    collection=dataBase[str(a)]
    collection.insert_many(re)
store()