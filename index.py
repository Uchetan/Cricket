from logger import logs
from toss import toss
from first_inning import first_inning
from second_inning import second_inning
from database import database
'''' IF YOU ARE USING FOR THE FIRST TIME PLZ PROVIDE YOUR MYSQL PASSWORD AND ANY DATABASE NAME AS PER YOURCHOICE
FOR ANY TYPE OF ERROR YOU CAN SEE THE LOG FILE named LOGS.DATA PRESENT AT THE LOGGER FOLDER'''
try:
    choice_1 = input('Enter your team name :- ')
    choice_2 = input('Enter your team name :- ')
    logs.lg.info('data entered sucessfuly :-  ' + 'team1 : ' + choice_1 + ': team2 :' + choice_2)


    print('====================================== Toss =======================================')
    tos_win, tos_los, act = toss.toss_ch(choice_1, choice_2)
    print('======================================***=========================================')
    ch = input(str(tos_win) + ' choice bat or ball :-')
    logs.lg.info(tos_win + ' choses to  : ' + ch)
    if ch == 'bat':
        print('======================================***=========================================')
        print('===============================First Innings=======================================')
        total1, wic_count, fir_bat, tea_1_bat, tea_2_bowl = first_inning.first_in(tos_win)
        print('======================================***=========================================')
        print('Score is :- ',total1," / ",wic_count )
        print('===============================Second Innings=======================================')
        total2, wic_count2, winner, sec_bat, tea_2_bat, tea_1_bowl = second_inning.sec_ing(tos_los, total1, tos_win)
        print('===============================match ends=======================================')
    else:
        print('======================================***=========================================')
        print('===============================First Innings=======================================')
        total1, wic_count, fir_bat, tea_1_bat, tea_2_bowl = first_inning.first_in(tos_los)
        print('======================================***=========================================')
        print('Score is :- ',total1," / ",wic_count )
        print('===============================Second Innings=======================================')
        total2, wic_count2, winner, sec_bat, tea_2_bat, tea_1_bowl = second_inning.sec_ing(tos_win, total1, tos_los)
        print('===============================match ends=======================================')

    print('======================================***=========================================')
    print(total1, ' / ', wic_count)
    tot1 = str(total1) + '/ ' + str(wic_count)
    print(fir_bat, 'scorecard', tea_1_bat)
    logs.lg.info(fir_bat + ' score : ' + str(total1))
    print(fir_bat, 'overs : ', tea_1_bowl)
    print("====================================================================================")
    print(total2, ' / ', wic_count2)
    tot2 = str(total2) + '/ ' + str(wic_count2)
    print(sec_bat, 'scorecard', tea_2_bat)
    logs.lg.info(sec_bat + ' score : ' + str(total2))
    print(sec_bat, 'overs : ', tea_2_bowl)

    print("=======================  ***   =============================")
    print('winner is  :- ', winner)
    if total2>total1:
        print(winner ,'won the match by : ', total2-total1,'runs')
    else:
        print(winner, 'won the match by : ' ,total1-total2,'runs')
    logs.lg.info('winner is : ' + winner)
    print("======================== ***  ============================")
    a = str(total1) + ' / ' + str(wic_count)
    b = str(total2) + ' / ' + str(wic_count2)
    ch = input('DO YOU WANT TO STORE THE MATCH DATA (Y/N) : ')
    if ch == 'y' or ch == 'Y':
        c = input('if it is your first time to store data(y/n) : -')
        if c == 'y' or c == 'Y':
            pas = input('Enter your MYSQl password : ')
            data_name = input('Enter the database name : ')
            database.first(pas, data_name)
        database.store(fir_bat, sec_bat, a, b, winner)
    else:
        print('THANKS FOR YOUR TIME')
    logs.lg.info('module runned sucessfully')
except Exception as e:
    print(e)
    print('error ocured please restart the program')
    logs.lg.error(e)
