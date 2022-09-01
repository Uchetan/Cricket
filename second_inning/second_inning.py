import random as rd
from logger import logs
wic=['bowled','catch out','lBW','RUN OUT']
runs=[0,0,1,1,1,2,2,2,3,3,4,4,4,6,6,6,6,6,0,0,1,1,2,2,2,8,8,8,8]
tea_2_bat={}
tea_1_bowl={}
def sec_ing(ch1,total1,ch):
    '''The Second innings is played here
    Pass 3 (second batting team name, Total of first team, First team name) variable'''
    logs.lg.info('second innings')
    stri=[]
    a=input(str(ch1)+' enter your first player :-')
    stri.append(a)
    tea_2_bat[a]=[]
    a=input(str(ch1)+' enter your second player :-')
    stri.append(a)
    tea_2_bat[a] = []
    p1=stri[0]
    total2 ,i,ov,wic_count= 0,1,0,0
    tea_1_bowl[ov]=[]
    fl=False
    while True:
        for i in range(1,7):
            input("\t\tPress enter to play the next ball : ")
            b=rd.choice(runs)
            if b!=8:
                if b==6 or b==4:
                    print(b, 'runs gained    !!!!!!')
                else:
                    print(b, 'runs gained')
                logs.lg.info(p1+' scored : '+str(b))
                total2=total2+b
                tea_2_bat[p1].append(b)
                if b==1 or b==3:
                    if p1==stri[0]:
                        p1=stri[1]
                    else:
                        p1=stri[0]
                tea_1_bowl[ov].append(b)
                if total2>total1:
                    fl=True
                    win=ch1
                    break
            else:
                c=rd.choice(wic)
                print('\t\t',p1,' wicket by ',c)
                wic_count = wic_count + 1
                print('\t\t',total2, " / ", wic_count)
                logs.lg.info(str(total2)+' / '+str(wic_count))
                if wic_count==9:
                    fl=True
                    break
                else:
                    a = input('\t\t'+str(ch1) + ' enter your player :- ')
                    stri.append(a)
                    tea_2_bat[a] = []
                if i!=6:
                    print("\t\tovers :- ",ov,'.',i)
                    print('\t\tto win : ',total1-total2," from ",((6-ov)*6)-i ,'balls')
                    logs.lg.info(' overs  :' + str(ov)+'.'+str(i))
                tea_1_bowl[ov].append(c)
                tea_2_bat[p1].append(c)
                stri.remove(p1)
                p1=stri[0]

        if ov != 4:
            if i==6:
                ov=ov+1
                tea_1_bowl[ov]=[]
                print('======================================Score=========================================')
                print(total2," / ",wic_count)
                logs.lg.info(str(total2)+' / '+str(wic_count))
                print('\t\tto win : ',total1-total2," from ",(6-ov)*6 ,'balls')
                print('overs :- ',ov)
                logs.lg.info(' overs  :' + str(ov))
                print('===============================================================================')
            elif total2>total1:
                win=ch1
            elif total1>total2:
                win=ch
            elif total1==total2:
                win='tie'
            else:
                continue
        else :
            if total2>total1:
                win=ch1
            else:
                win=ch
            break
        if fl==True:
            break
    logs.lg.info('second inning ends sucessfully')
    return total2,wic_count,win,ch1,tea_2_bat,tea_1_bowl