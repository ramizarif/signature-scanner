import pandas, menus, start, scans, fill
from graphics import * 

def main(): 

    program = True
    while program == True: 
        select = menus.mainMenu()
        if select == False: 
            var = start.start()
            if var == 'hp': 
                finalData, fileName = scans.scanMain()
                fill.fillIn(finalData, fileName)
                

        elif select == True: 
            print('ramiz get working on the about screen!')
        else: 
            program = False

main()

#HP Spectre Folio - 13-ak0001na, MYL123456789, 5ES85EA#ABA, 10y0
#HP Spectre Folio - 13-ak0001na, MYL456789124, 5Bs865A#ABA, 10y0





    

    