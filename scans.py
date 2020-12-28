#create the scanner and use pandas here 
'''
task list: 
- create interface with entry boxes
- take scan from entry box 
- seperate the product id and serial number from everything else
- prompt for problem 
- append this data into a list
- create big list with sub lists for items that need to be appended into rows together
- open blank template file for reading 
- modify it by adding the sublists in each row where they belong (iterate through each row)

other things to consider: 
-hp and acer will have specific ways to split the data
-custom will have elements determined by user, will take info from the custom menu
'''
import pandas 
from graphics import* 

def clicked(click, rect):

    #if no mouse click was detected we return false
    if not click:
        return False

    #Gets points 1 and 2 of the corners of the rectangle 
    point1 = rect.getP1()
    point2 = rect.getP2()

    #If the x coordinate is > first point and less than second point and the Y coordinate is > first point and less than second point return true
    return (point1.getX() < click.getX() < point2.getX()) and (point1.getY() < click.getY() < point2.getY())

def press(keyPress, key):

    if not keyPress:
        return False

    return keyPress == key

def scanScreen(): 

    win = GraphWin('Signature Scanner', 500, 500)
    win.setCoords(0, 0, 500, 500)

    #will have to change this text for each scan 
    scanText = Text(Point(250, 400), 'Scan #1') 
    scanText.setSize(20)
    scanText.setStyle('bold')
    scanText.draw(win)

    moreText = Text(Point(250, 320), 'Product Scan')
    moreText.setStyle('italic')
    moreText.draw(win)

    #create the entry boxes that the scan will be taken from
    scanEntry = Entry(Point(250, 300), 20)
    scanEntry.draw(win)

    prodID = Text(Point(150, 200), 'Product ID')
    prodID.setStyle('italic')
    prodID.draw(win)

    prodEntry = Entry(Point(150, 180), 10)
    prodEntry.draw(win)

    serial = Text(Point(350, 200), 'Serial Number')
    serial.setStyle('italic')
    serial.draw(win)

    serialEntry = Entry(Point(350, 180), 10)
    serialEntry.draw(win)

    nextRect = Rectangle(Point(200, 80), Point(300, 120))
    nextRect.setFill('green')
    cenx = nextRect.getCenter().getX()
    ceny = nextRect.getCenter().getY()
    nextText = Text(Point(cenx, ceny), 'Next')
    nextText.setTextColor('white')
    nextText.setStyle('bold')
    nextRect.draw(win)
    nextText.draw(win)

    finRect = Rectangle(Point(300, 0), Point(500, 40))
    finRect.setFill('blue')
    cenx = finRect.getCenter().getX()
    ceny = finRect.getCenter().getY()
    finText = Text(Point(cenx, ceny), 'Finished Scanning')
    finText.setSize(12)
    finText.setTextColor('white')
    finText.setStyle('italic')
    finRect.draw(win)
    finText.draw(win)

    return scanEntry, prodEntry, serialEntry, nextRect, finRect, scanText, win

def hpScan(scanEntry): 

    data = {}
    temp = []

    #HP Spectre Folio - 13-ak0001na, MYL123456789, 5ES85EA#ABA, 10y0
    try:
        temp = scanEntry.split(',') 
        for item in temp: 
            if 'HP' in item: 
                temp.remove(item)
                del temp[-1]
        for i in range (0, len(temp)): 
           for z in temp :
                if 'ABA' in z: 
                   data['productID'] = z
                elif 'ABA' not in z: 
                    data['serial'] = z
        
    except: 
        data = {'serial': '', 'productID': ''}

    return data

def prompt(): 
    win = GraphWin('Issue', 300, 200)
    win.setCoords(0, 0, 300, 200)

    qText = Text(Point(150, 120), 'What is the problem with the device?')
    qText.draw(win)

    qEntry = Entry(Point(150, 100), 20)
    qEntry.draw(win)

    enterText = Text(Point(150, 80), 'Click Enter to Continue')
    enterText.draw(win)

    keyPress = win.checkKey()
    while(press(keyPress, 'Return') == False): 
        keyPress = win.checkKey()
    else: 
        problem = qEntry.getText()
        win.close()

    return problem


def scanMain(): 

    #initialize a list for the data that will be inserted into the rows in excel 
    subData = []
    finalData = []

    #
    scanEntry, prodEntry, serialEntry, nextRect, finRect, scanText, win = scanScreen()
    #scan = scanEntry.getText()
    click = win.checkMouse()
    count = 1
    while clicked(click, finRect) == False: 
        scan = scanEntry.getText()
        data = hpScan(scan)
        subData = []
        try: 
            serialEntry.setText(data['serial'])
            prodEntry.setText(data['productID'])

        except: 
            pass

        if clicked(click, nextRect): 
                count += 1
                subData.append(serialEntry.getText())
                subData.append(prodEntry.getText())
                problem = prompt()
                subData.append(problem)
                finalData.append(subData)
                scanEntry.setText('')
                prodEntry.setText('')
                scanText.setText = 'Scan #' + str(count)
        else: 
            click = win.checkKey()

        click = win.checkMouse()
    else: 
        try: 
            finalData.append(subData)
            subData.append(serialEntry.getText())
            subData.append(prodEntry.getText())
        except: 
            pass
        fileName = modFile()
        win.close()
    
    for element in finalData: 
        if element == ['', '']: 
            finalData.remove(element)

    return finalData, fileName

#scanMain()

def modFile(): 

    win = GraphWin('Signature Scanner', 300, 200)
    win.setCoords(0, 0, 300, 200)

    qText = Text(Point(150, 120), 'Write in a name for the Excel File.')
    qText.draw(win)

    qEntry = Entry(Point(150, 100), 20)
    qEntry.draw(win)

    enterText = Text(Point(150, 80), 'Click Enter to Continue.')
    enterText.draw(win)

    keyPress = win.checkKey()
    while(press(keyPress, 'Return') == False): 
        keyPress = win.checkKey()
    else: 
        fileName = qEntry.getText()
        win.close()

    return fileName



#HP Spectre Folio - 13-ak0001na, MYL123456789, 5ES85EA#ABA, 10y0
#HP Spectre Folio - 13-ak0001na, MYL456789124, 5Bs865A#ABA, 10y0













