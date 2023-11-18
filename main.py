import mss.tools
import os
import time as t
import mouse
import keyboard
import pyautogui

os.system("cls")
laptop = True

class coord():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
class box():
    def __init__(self, x1,y1,x2,y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        
class building():
    def __init__(self, coordinates, baseColor, buyableColor, translatedCoordinates, baseCost, cps):
        self.coords = coordinates
        self.x = coordinates.x
        self.y = coordinates.y
        self.color1 = baseColor
        self.color2 = buyableColor
        self.tX = translatedCoordinates.x
        self.tY = translatedCoordinates.y
        self.cost = baseCost
        self.cps = cps

def click(x,y,times):
    if (mouse.get_position() != (x,y)):
        mouse.move(x,y)
    
    for _ in range(times):
        if (mouse.get_position()[0] >= x+10 or mouse.get_position()[0] <= x-10 or mouse.get_position()[1] >= y+10 or mouse.get_position()[1] <= y-10):
            return False
        
        mouse.click()
        t.sleep(0.005)
        
    return True

def costCalc(builds, buildings, build):
    costs = []
    i = 0
    for b in builds:
        b = float(b)
        if (b == 0):
            pass
        else:
            costs.append(buildings[i].cps/(buildings[i].cost*1.15**b))
        i+=1

    cost = build.cps/(build.cost*1.15**builds[buildings.index(build)])
    
    for c in costs:
        if (cost >= c):
            pass
        else:
            return False
        
    return True

def main():
    builds = []

    with open("builds.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            builds.append(int(line))

    running = False

    if (not laptop):
        buildingBox = box(1788,305,1864,805)
        cookie = coord(325, 485)
        cursor = building(coord(35,20), (102,108,105), (158,152,136), coord(1780,330), 15, 0.1)
        grandma = building(coord(35,85), (91,98,96), (143,136,120), coord(1780,400), 100, 1)
        farm = building(coord(35,150), (94,102,100), (144,141,126), coord(1780,460), 1100, 8)
        mine = building(coord(35,215), (102,109,103), (159,153,131), coord(1780, 525), 12000, 47)
        factory = building(coord(35,280), (94,101,99), (145,139,123), coord(1780, 590), 130000, 260)
        bank = building(coord(35,345), (93,100,97), (144,137,121), coord(1780, 650), 1400000, 1400)
        temple = building(coord(35,405), (89,99,98), (141,138,123), coord(1780, 715), 20000000, 7800)
        wizard = building(coord(35,470), (101,109,103), (), coord(1780, 780), 330000000, 44000)
        upgrade = coord(1655,195)


        chromePos = [520,1060]
        mouse.move(chromePos[0],chromePos[1], 0.5)
        mouse.click()

    if (laptop):
        buildingBox = box(1245,200,1348,767)
        upgrade = coord(1105,94)
        cookie = coord(209,320)
        cursor = building(coord(35,20), (), (154,152,130), coord(1265,230), 15, 0.1)
        grandma = building(coord(35,85), (), (131,130,112), coord(1265,300), 100, 1)
        farm = building(coord(35,150), (), (137,134,117), coord(1265,360), 1100, 8)
        mine = building(coord(35,215), (), (152,147,127), coord(1265, 420), 12000, 47)
        factory = building(coord(35,280), (), (150,143,123), coord(1265, 490), 130000, 260)
        bank = building(coord(35,345), (), (132,129,112), coord(1265, 550), 1400000, 1400)
        temple = building(coord(35,405), (), (135,132,115), coord(1265, 615), 20000000, 7800)
        wizard = building(coord(35,470), (), (151,146,126), coord(1265, 680), 330000000, 44000)
        shipment = building(coord(35,540), (), (152,145,126), coord(1265,750), 5100000000, 260000)

        chromePos = [880,740]
        mouse.move(chromePos[0],chromePos[1], 0.5)
        mouse.click()

        keyboard.press_and_release("F11")
    
    buildingArray = [cursor, grandma, farm, mine, factory, bank, temple, wizard, shipment]

    t.sleep(1)

    with mss.mss() as sct:
        buildings = {"top":buildingBox.y1, "left":buildingBox.x1, "width":buildingBox.x2-buildingBox.x1, "height":buildingBox.y2-buildingBox.y1}
        upgrades = {"top":upgrade.y, "left":upgrade.x, "width":1, "height":1}
        output = "testScreenshot.png"
        
        #pic = sct.grab(buildings)
        #print(pic.pixel(cursor.x,cursor.y))
        #print(pic.pixel(grandma.x,grandma.y))
        #print(pic.pixel(farm.x,farm.y))
        #print(pic.pixel(mine.x,mine.y))
        #print(pic.pixel(factory.x,factory.y))
        #print(pic.pixel(bank.x,bank.y))
        #print(pic.pixel(temple.x,temple.y))
        #print(pic.pixel(wizard.x,wizard.y))
        #print(pic.pixel(shipment.x,shipment.y))
        #mss.tools.to_png(pic.rgb,pic.size, output=output)

        #pic = sct.grab(upgrades)
        #print(pic.pixel(0,0))
        #mss.tools.to_png(pic.rgb,pic.size,output=output)
        
        while True:
            if (keyboard.is_pressed("c")):
                running = True
                
            if (keyboard.is_pressed("esc")):
                break
            
            if (running):
                pic2 = sct.grab(upgrades)
                
                if (pic2.pixel(0,0) == (235,204,170)):
                    click(upgrade.x,upgrade.y, 5)
                    
                pic = sct.grab(buildings)

                if (pic.pixel(shipment.x,shipment.y) == shipment.color2 and (costCalc(builds,buildingArray,shipment) or builds[8] == 0)):
                    click(shipment.tX,shipment.tY,1)
                    builds[8] += 1
                elif (pic.pixel(wizard.x,wizard.y) == wizard.color2 and (costCalc(builds,buildingArray,wizard) or builds[7] == 0)):
                    click(wizard.tX,wizard.tY,1)
                    builds[7] += 1
                elif (pic.pixel(temple.x,temple.y) == temple.color2 and (costCalc(builds,buildingArray,temple) or builds[6] == 0)):
                    click(temple.tX,temple.tY,1)
                    builds[6] += 1
                elif (pic.pixel(bank.x,bank.y) == bank.color2 and (costCalc(builds,buildingArray,bank) or builds[5] == 0)):
                    click(bank.tX,bank.tY,1)
                    builds[5] += 1
                elif (pic.pixel(factory.x,factory.y) == factory.color2 and (costCalc(builds,buildingArray,factory) or builds[4] == 0)):
                    click(factory.tX,factory.tY,1)
                    builds[4] += 1
                elif (pic.pixel(mine.x,mine.y) == mine.color2 and (costCalc(builds,buildingArray,mine) or builds[3] == 0)):
                    click(mine.tX,mine.tY,1)
                    builds[3] += 1
                elif (pic.pixel(farm.x,farm.y) == farm.color2 and (costCalc(builds,buildingArray,farm) or builds[2] == 0)):
                    click(farm.tX,farm.tY,1)
                    builds[2] += 1
                elif (pic.pixel(grandma.x,grandma.y) == grandma.color2 and (costCalc(builds,buildingArray,grandma) or builds[1] == 0)):
                    click(grandma.tX,grandma.tY,1)
                    builds[1] += 1
                elif (pic.pixel(cursor.x,cursor.y) == cursor.color2 and (costCalc(builds,buildingArray,cursor) or builds[0] == 0)):
                    click(cursor.tX,cursor.tY,1)
                    builds[0] += 1
                    
                running = click(cookie.x,cookie.y, 100)
                
        with open("builds.txt", "w") as file:
            for b in builds:
                file.write(str(b) + "\n")

if __name__ == "__main__":
    main()