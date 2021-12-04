import random as rd
from logger import logs
def toss_ch(choice_1,choice_2):
    '''
    function is written to decide how wins the toss for the match
    '''
    try:
        tos = ['head', 'tail']
        ch_1=input(str(choice_1)+' enter your choice (head / tail) :- ')
        print('======================================***=========================================')
        a=rd.choice(tos)
        print('the coin rolls to :-',a)
        logs.lg.info('coin rolled was : '+a)
        print('======================================***=========================================')
        if a==ch_1:
            win=choice_1
            los=choice_2
        else:
            win=choice_2
            los=choice_1
        print('Toss is winned by : ',win)
        logs.lg.info('toss was winned by : '+win)
        return win,los,a
    except Exception as e:
        logs.lg.error('error occured at database : '+str(e))