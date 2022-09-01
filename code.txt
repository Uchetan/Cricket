from logger import logs
# To maintain log file
from toss import toss
# Returns the Toss winner
# Needs Two argument (Two team names)
# Return three arguments (Winner,Losser,Coin Rolled)
from first_inning import first_inning
# the entire first inning is played here
# Needs single argument(first one to bat)
# returns 5 arguments (Total [total1] , , batting scorecard [tea_1_bat], total over played [tea_2_bowl])
from second_inning import second_inning
# the entire first inning is played here
# Needs 3 argument (Second team to bat, Target to chase, Bowling team)
# returns 6 arguments (Total of team2 [total2] ,Wicket count [wic_count2],Winner [winner], batting scorecard [tea_2_bat], total over played [tea_1_bowl])
from database import database
# use to store the cricket data
# Needs 5 argument (team First bat [fir_bat], Team second to bat [sec_bat],
# str of total/wicket count [a],str of total/wicket count b, winner [winner],Mysql local database Password [pas]
'''' IF YOU ARE USING FOR THE FIRST TIME PLZ PROVIDE YOUR MYSQL PASSWORD AND ANY DATABASE NAME AS PER YOURCHOICE
FOR ANY TYPE OF ERROR YOU CAN SEE THE LOG FILE named LOGS.DATA PRESENT AT THE LOGGER FOLDER '''
try:
    choice_1 = input('Enter your team name :- ')  # takes input from the user for the team name
    choice_2 = input('Enter your team name :- ')  # takes input from the user for the second team name
    logs.lg.info('data entered sucessfully :-  ' + 'team1 : ' + choice_1 + ': team2 :' + choice_2)
    print('====================================== Toss =======================================')
    tos_win, tos_los, act = toss.toss_ch(choice_1, choice_2)  # toss module is called for the toss
    print('======================================***=========================================')
    ch = input(str(tos_win) + ' choice bat or ball :-') # takes input to decide how will bat first
    logs.lg.info(tos_win + ' choses to  : ' + ch)
    if ch == 'bat':
        print('======================================***=========================================')
        print('===============================First Innings=======================================')
        total1, wic_count, fir_bat, tea_1_bat, tea_2_bowl = first_inning.first_in(tos_win)
        #calls first_inning module
        print('======================================***=========================================')
        print('Score is :- ',total1," / ",wic_count )
        print('===============================Second Innings=======================================')
        total2, wic_count2, winner, sec_bat, tea_2_bat, tea_1_bowl = second_inning.sec_ing(tos_los, total1, tos_win)
        #calls the second_inning module
        print('===============================match ends=======================================')
    else:
        print('======================================***=========================================')
        print('===============================First Innings=======================================')
        total1, wic_count, fir_bat, tea_1_bat, tea_2_bowl = first_inning.first_in(tos_los)
        #calls first_inning module
        print('======================================***=========================================')
        print('Score is :- ',total1," / ",wic_count )
        print('===============================Second Innings=======================================')
        total2, wic_count2, winner, sec_bat, tea_2_bat, tea_1_bowl = second_inning.sec_ing(tos_win, total1, tos_los)
        #calls the second_inning module
        print('===============================match ends=======================================')
# displays the Scorecard for the First team
    print('======================================***=========================================')
    print(total1, ' / ', wic_count)
    tot1 = str(total1) + '/ ' + str(wic_count)
    print(fir_bat, 'scorecard', tea_1_bat)
    logs.lg.info(fir_bat + ' score : ' + str(total1))
    print(fir_bat, 'overs : ', tea_1_bowl)
    print("====================================================================================")
#displays the Scorecard for the Second team
    print(total2, ' / ', wic_count2)
    tot2 = str(total2) + '/ ' + str(wic_count2)
    print(sec_bat, 'scorecard', tea_2_bat)
    logs.lg.info(sec_bat + ' score : ' + str(total2))
    print(sec_bat, 'overs : ', tea_2_bowl)
#diplays the Winner
    print("=======================  ***   =============================")
    print('/t/twinner is  :- ', winner)
    if total2>total1:
        print(winner ,'won the match by : ', total2-total1,'runs')
    else:
        print(winner, 'won the match by : ' ,total1-total2,'runs')
    logs.lg.info('winner is : ' + winner)
    print("======================== ***  ============================")
    a = str(total1) + ' / ' + str(wic_count)
    b = str(total2) + ' / ' + str(wic_count2)
#To save the match result in the MySql Database
    ch = input('DO YOU WANT TO STORE THE MATCH DATA (Y/N) : ')
    if ch == 'y' or ch == 'Y':
        #Asks if Data is saved First time
        c = input('if it is your first time to store data(y/n) : -')
        if c == 'y' or c == 'Y':
            pas = input('Enter your MYSQl password : ')
            database.first(pas)
            try:
                database.store(fir_bat, sec_bat, a, b, winner,pas)
                print('Data saved')
            except Exception as e:
                print(e)
        else:
            try:
                pas = input('Enter your MYSQl password : ')
                database.store(fir_bat, sec_bat, a, b, winner,pas)
                print("Data saved")
            except Exception as e:
                print(e)
    else:
        print('THANKS FOR YOUR TIME')
    logs.lg.info('module runned sucessfully')
except Exception as e:
    print(e)
    print('error ocured please restart the program')
    logs.lg.error(e)
