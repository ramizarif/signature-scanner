from graphics import *

def clicked(click, rect):

    #if no mouse click was detected we return false
    if not click:
        return False

    #Gets points 1 and 2 of the corners of the rectangle 
    point1 = rect.getP1()
    point2 = rect.getP2()

    #If the x coordinate is > first point and less than second point and the Y coordinate is > first point and less than second point return true
    return (point1.getX() < click.getX() < point2.getX()) and (point1.getY() < click.getY() < point2.getY())

def mainMenu(): 

    #------------------------------------------------------
    #creation of the main menu of Signature Scanner
    #Signature Scanner will include start scanning, about menu, and an exit button

    win = GraphWin('Signature Scanner', 500, 500)
    win.setCoords(0, 0, 500, 500)
    win.setBackground('light grey')

    title = Text(Point(250, 400), 'Signature Scanner')
    title.setSize(24)
    title.setStyle('bold')
    title.draw(win)

    startp1 = 80
    startp2 = 120
    startRect = Rectangle(Point(250 - startp1, 250 + 100 - startp2), Point(250 + startp1, 250 + 100 - startp1))
    startRect.setFill('green')
    cenx = startRect.getCenter().getX()
    ceny = startRect.getCenter().getY()
    startText = Text(Point(cenx, ceny), 'Start Scanning')
    startText.setTextColor('black')
    startText.setStyle('bold')
    startRect.draw(win)
    startText.draw(win)

    aboutp1 = 80
    aboutp2 = 120
    aboutRect = Rectangle(Point(250 - startp1, 250 + 50 - startp2), Point(250 + startp1, 250 + 50 - startp1))
    aboutRect.setFill('blue')
    cenx =aboutRect.getCenter().getX()
    ceny = aboutRect.getCenter().getY()
    aboutText = Text(Point(cenx, ceny), 'About')
    aboutText.setTextColor('black')
    aboutText.setStyle('bold')
    aboutRect.draw(win)
    aboutText.draw(win) 

    quitp1 = 80
    quitp2 = 120
    quitRect = Rectangle(Point(250 - startp1, 250  - startp2), Point(250 + startp1, 250 - startp1))
    quitRect.setFill('red')
    cenx =quitRect.getCenter().getX()
    ceny = quitRect.getCenter().getY()
    quitText = Text(Point(cenx, ceny), 'Exit')
    quitText.setTextColor('black')
    quitText.setStyle('bold')
    quitRect.draw(win)
    quitText.draw(win)

    click = win.checkMouse()
    while clicked(click, quitRect) == False: 
        if clicked(click, startRect): 
            win.close()
            return False
        elif clicked(click, aboutRect): 
            win.close()
            return False
        else: 
            click = win.checkMouse()


    #-------------------------------------------------------------------------------------------------------------------------------------------










