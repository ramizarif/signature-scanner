import pandas, menus, start
from graphics import * 

def main(): 

    program = True
    while program == True: 
        select = menus.mainMenu()
        if select == False: 
            s = start.start()
        elif select == True: 
            print('ramiz get working on the about screen!')
        else: 
            program = False

main()





    

    