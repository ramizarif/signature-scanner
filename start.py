import pandas
import scans
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


def start(): 

    win = GraphWin('Signature Scanner', 500, 500)
    win.setCoords(0, 0, 500, 500)
    win.setBackground('light grey')

    choose = Text(Point(250, 400), 'What type of product are you scanning?')
    choose.setStyle('italic')
    choose.setSize(14)
    choose.draw(win)

    hpp1 = 80
    hpp2 = 120
    hpRect = Rectangle(Point(250 - hpp1, 250 + 100 - hpp2), Point(250 + hpp1, 250 + 100 - hpp1))
    hpRect.setFill('silver')
    cenx = hpRect.getCenter().getX()
    ceny = hpRect.getCenter().getY()
    hpText = Text(Point(cenx, ceny), 'HP Scanner')
    hpText.setTextColor('black')
    hpText.setStyle('bold')
    hpRect.draw(win)
    hpText.draw(win)


    exitp1 = 80
    exitp2 = 120
    exitRect = Rectangle(Point(250 - exitp1, 250 - 50 - exitp2), Point(250 + exitp1, 250 - 50 - exitp1))
    exitRect.setFill('red')
    cenx = exitRect.getCenter().getX()
    ceny = exitRect.getCenter().getY()
    exitText = Text(Point(cenx, ceny), 'Exit')
    exitText.setTextColor('black')
    exitText.setStyle('bold')
    exitRect.draw(win)
    exitText.draw(win)

    var = ''

    click = win.checkMouse()
    while clicked(click, exitRect) == False: 
        if clicked(click, hpRect):
            win.close() 
            var = 'hp'
            return var
        else: 
            click = win.checkMouse()
    else: 
        win.close()


    