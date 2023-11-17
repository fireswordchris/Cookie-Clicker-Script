import mss.tools
import os
import time as t
import mouse
import keyboard
import pyautogui

os.system("cls")

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
    def __init__(self, coordinates, baseColor, buyableColor, translatedCoordinates):
        self.coords = coordinates
        self.x = coordinates.x
        self.y = coordinates.y
        self.color1 = baseColor
        self.color2 = buyableColor
        self.tX = translatedCoordinates.x
        self.tY = translatedCoordinates.y

def click(x,y,times):
    if (mouse.get_position() != (x,y)):
        mouse.move(x,y)
    
    for _ in range(times):
        if (mouse.get_position()[0] >= x+10 or mouse.get_position()[0] <= x-10 or mouse.get_position()[1] >= y+10 or mouse.get_position()[1] <= y-10):
            return False
        
        mouse.click()
        t.sleep(0.0025)
        
    return True

def main():
    builds = []
    
    with open("builds.txt","r") as file:
        lines = file.readlines()
        for line in lines:
            builds.append(int(line))
    
    buildingBox = box(1788,305,1864,1040)
    cookie = coord(325, 485)
    cursor = building(coord(35,20), (102,108,105), (158,152,136), coord(1780,330))
    grandma = building(coord(35,85), (91,98,96), (143,136,120), coord(1780,400))
    farm = building(coord(35,150), (94,102,100), (144,141,126), coord(1780,460))
    mine = building(coord(35,215), (102,109,103), (159,153,131), coord(1780, 525))
    factory = building(coord(35,280), (94,101,99), (145,139,123), coord(1780, 590))
    bank = building(coord(35,345), (93,100,97), (144,137,121), coord(1780, 650))
    temple = building(coord(35,405), (89,99,98), (141,138,123), coord(1780, 715))
    wizard = building(coord(35,485), (101,109,103), (152,149,132), coord(1780, 780))
    shipment = building(coord(35,540), (99,107,103), (154,148,132), coord(1780,845))
    lab = building(coord(35,605), (94,103,99), (143,138,119), coord(1780,910))
    portal = building(coord(35,670), (93,102,100), (145,143,130), coord(1780,975))
    time = building(coord(35,720), (81,84,79), (131,126,11), coord(1780,1030))
    upgrade = coord(1655,195)
    
    running = False
    
    
    chromePos = [520,1060]
    mouse.move(chromePos[0],chromePos[1], 0.5)
    mouse.click()
    
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
        #print(pic.pixel(lab.x,lab.y))
        #print(pic.pixel(portal.x,portal.y))
        #print(pic.pixel(time.x,time.y))
        #mss.tools.to_png(pic.rgb,pic.size, output=output)
        
        while True:
            if (keyboard.is_pressed("c")):
                running = True
                
            if (keyboard.is_pressed("esc")):
                break
            
            if (running):
                pic2 = sct.grab(upgrades)
                
                if (pic2.pixel(0,0) == (235,203,169)):
                    click(upgrade.x,upgrade.y, 2)
                    
                pic = sct.grab(buildings)
                
                if (pic.pixel(time.x,time.y) == time.color2 and builds[11] <= 40):
                    click(time.tX,time.tY,1)
                    builds[11] += 1
                elif (pic.pixel(portal.x,portal.y) == portal.color2 and builds[10] <= 40):
                    click(portal.tX,portal.tY,1)
                    builds[10] += 1
                elif (pic.pixel(lab.x,lab.y) == lab.color2 and builds[9] <= 40):
                    click(lab.tX,lab.tY,1)
                    builds[9] += 1
                elif (pic.pixel(shipment.x,shipment.y) == shipment.color2 and builds[8] <= 40):
                    click(shipment.tX,shipment.tY,1)
                    builds[8] += 1
                elif (pic.pixel(wizard.x,wizard.y) == wizard.color2 and builds[7] <= 40):
                    click(wizard.tX,wizard.tY,1)
                    builds[7] += 1
                elif (pic.pixel(temple.x,temple.y) == temple.color2 and builds[6] <= 40):
                    click(temple.tX,temple.tY,1)
                    builds[6] += 1
                elif (pic.pixel(bank.x,bank.y) == bank.color2 and builds[5] <= 40):
                    click(bank.tX,bank.tY,1)
                    builds[5] += 1
                elif (pic.pixel(factory.x,factory.y) == factory.color2 and builds[4] <= 40):
                    click(factory.tX,factory.tY,1)
                    builds[4] += 1
                elif (pic.pixel(mine.x,mine.y) == mine.color2 and builds[3] <= 40):
                    click(mine.tX,mine.tY,1)
                    builds[3] += 1
                elif (pic.pixel(farm.x,farm.y) == farm.color2 and builds[2] <= 40):
                    click(farm.tX,farm.tY,1)
                    builds[2] += 1
                elif (pic.pixel(grandma.x,grandma.y) == grandma.color2 and builds[1] <= 40):
                    click(grandma.tX,grandma.tY,1)
                    builds[1] += 1
                elif (pic.pixel(cursor.x,cursor.y) == cursor.color2 and builds[0] <= 50):
                    click(cursor.tX,cursor.tY,1)
                    builds[0] += 1
                    
                running = click(cookie.x,cookie.y, 100)
                
        with open("builds.txt","w") as file:
            for b in builds:
                file.write(str(b) + "\n")
                
    
if __name__ == "__main__":
    main()