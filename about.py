from graphics import *

def aboutScreen(): 

    win = GraphWin('Signature Scanner', 800, 600)
    win.setCoords(0, 0, 500, 500)
    win.setBackground('light grey')

    title = Text(Point(250, 400), 'Instructions')
    title.setSize(24)
    title.setStyle('bold')
    title.draw(win)

    x = 250
    y = 350
    dy = -20
    desc = Text(Point(250, 350), 'This program will split the necessary data from a scan on faulty equipment.')
    desc2 = Text(Point(x, y + dy), 'Start by scanning the product in the Scan Entrybox.')
    desc3 = Text(Point(x, y + (dy*2)), 'Proceed by clicking the Next Button and detailing what is wrong with the computer.')
    desc4 = Text(Point(x, y + (dy *3)), 'Once all products have been scanned click finish scanning.')
    desc5 = Text(Point(x, y + (dy*4)), 'Then type in the desired Final Name.')
    desc6 = Text(Point(x,y + (dy*5)), 'You can then find the Excel file in the same folder as the Signature Scanner.' )
    
    desc.draw(win)
    desc2.draw(win)
    desc3.draw(win)
    desc4.draw(win)
    desc5.draw(win)
    desc6.draw(win)

    click = win.getMouse()
    win.close()

aboutScreen()