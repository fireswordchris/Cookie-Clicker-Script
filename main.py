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
    buildingBox = box(1788,305,1864,805)
    cookie = coord(325, 485)
    cursor = building(coord(35,20), (102,108,105), (158,152,136), coord(1780,330))
    grandma = building(coord(35,85), (91,98,96), (143,136,120), coord(1780,400))
    farm = building(coord(35,150), (94,102,100), (144,141,126), coord(1780,460))
    mine = building(coord(35,215), (102,109,103), (159,153,131), coord(1780, 525))
    factory = building(coord(35,280), (94,101,99), (145,139,123), coord(1780, 590))
    bank = building(coord(35,345), (93,100,97), (144,137,121), coord(1780, 650))
    temple = building(coord(35,405), (89,99,98), (141,138,123), coord(1780, 715))
    wizard = building(coord(35,470), (101,109,103), (), coord(1780, 780))
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
        
        #pic = sct.grab(monitor)
        #print(pic.pixel(cursor.x,cursor.y))
        #print(pic.pixel(grandma.x,grandma.y))
        #print(pic.pixel(farm.x,farm.y))
        #print(pic.pixel(mine.x,mine.y))
        #print(pic.pixel(factory.x,factory.y))
        #print(pic.pixel(bank.x,bank.y))
        #print(pic.pixel(temple.x,temple.y))
        #print(pic.pixel(wizard.x,wizard.y))
        #mss.tools.to_png(pic.rgb,pic.size, output=output)
        
        while True:
            if (keyboard.is_pressed("c")):
                running = True
                
            if (keyboard.is_pressed("esc")):
                break
            
            if (running):
                pic = sct.grab(buildings)
                pic2 = sct.grab(upgrades)
                
                if (pic2.pixel(0,0) == (235,203,169)):
                    click(upgrade.x,upgrade.y, 2)
                
                if (pic.pixel(temple.x,temple.y) == temple.color2):
                    click(temple.tX,temple.tY,15)
                elif (pic.pixel(bank.x,bank.y) == bank.color2):
                    click(bank.tX,bank.tY,15)
                elif (pic.pixel(factory.x,factory.y) == factory.color2):
                    click(factory.tX,factory.tY,15)
                elif (pic.pixel(mine.x,mine.y) == mine.color2):
                    click(mine.tX,mine.tY,15)
                elif (pic.pixel(farm.x,farm.y) == farm.color2):
                    click(farm.tX,farm.tY,15)
                elif (pic.pixel(grandma.x,grandma.y) == grandma.color2):
                    click(grandma.tX,grandma.tY,15)
                elif (pic.pixel(cursor.x,cursor.y) == cursor.color2):
                    click(cursor.tX,cursor.tY,15)
                    
                running = click(cookie.x,cookie.y, 1000)
                
    
if __name__ == "__main__":
    main()