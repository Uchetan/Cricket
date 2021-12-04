import random as rd
from logger import logs
wic=['bowled','catch out','lBW','RUN OUT']
runs=[0,0,1,1,1,2,2,2,3,3,4,4,4,6,6,6,6,6,0,0,1,1,2,2,2,8,8,8,8]
tea_1_bat = {}
tea_2_bowl = {}
def first_in(ch):
    stri=[]
    logs.lg.info('first ining')
    a=input(str(ch)+' enter your first player :-')
    stri.append(a)
    tea_1_bat[a]=[]
    a=input(str(ch)+' enter your second player :-')
    stri.append(a)
    tea_1_bat[a] = []
    p1=stri[0]
    total1 ,i,ov,wic_count= 0,1,0,0
    tea_2_bowl[ov]=[]
    fl=False
    while True:
        for i in range(1,7):
            f22=False
            b=rd.choice(runs)
            if b!=8:
                if b==6 or b==4:
                    print(b, 'runs gained    !!!!!!')
                else:
                    print(b, 'runs gained')
                logs.lg.info(p1+' scored : '+str(b))
                total1=total1+b
                tea_1_bat[p1].append(b)
                if b==1 or b==3:
                    if p1==stri[0]:
                        p1=stri[1]
                    else:
                        p1=stri[0]
                tea_2_bowl[ov].append(b)
            elif b==8:
                c=rd.choice(wic)
                wic_count = wic_count + 1
                print("\t\t", total1, " / ", wic_count)
                print('\t\t',p1,'wicket by ',c)
                if wic_count==9:
                    fl=True
                    break
                else:
                    a = input('\t\t'+str(ch) + ' enter your player :- ')
                    stri.append(a)
                    tea_1_bat[a] = []
                logs.lg.info(str(total1)+' / '+str(wic_count))
                if i!=6:
                    print("\t\tovers :- ",ov,'.',i)
                    logs.lg.info(' overs  :' + str(ov)+'.'+str(i))
                tea_2_bowl[ov].append(c)
                tea_1_bat[p1].append(c)
                stri.remove(p1)
                p1=stri[0]

        if ov != 4:
            if i==6 :
                ov=ov+1
                print('======================================Score=========================================')
                tea_2_bowl[ov]=[]
                print(total1, " / ", wic_count)
                logs.lg.info(str(total1)+' / '+str(wic_count))
                print('overs :- ',ov)
                print('===================================================================================')
                logs.lg.info(' overs  :'+str(ov))
            else:
                continue
        else :
            break
        if fl==True:
            break
    logs.lg.info('first inning ends sucessfully')
    return total1,wic_count,ch,tea_1_bat,tea_2_bowl