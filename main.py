import mss.tools
import os
import time as t
import mouse
import keyboard
import pyautogui
import tkinter as tk
#13 seconds between golden cookie spawn and despawn
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
    def __init__(self, name, coordinates, baseColor, buyableColor, translatedCoordinates, baseCost, cps):
        self.name = name
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
        t.sleep(0.0025)
        
    return True

def costCalc(builds, buildings, build, cps):
    costs = []
    i = 0
    for b in builds:
        b = float(b)
        if (b == 0):
            pass
        else:
            costs.append(cps[i]/(buildings[i].cost*1.15**b))
        i+=1

    cost = cps[buildings.index(build)]/(build.cost*1.15**builds[buildings.index(build)])
    
    for c in costs:
        if (cost >= c):
            pass
        else:
            return False
        
    return True

def calcAllCosts(builds, buildings, cps):
    costs = []
    i = 0
    tempBuild = buildings[0]
    
    for b in builds:
        b = int(b)
        
        if (b == 0):
            pass
        else:
            costs.append(cps[i]/(buildings[i].cost*1.15**b))
        i+=1
    
    print(costs)
    for build in buildings:
        if (builds[buildings.index(build)] > 0):
            cost = costs[buildings.index(build)]
            for c in costs:
                if (cost >= c):
                    if (costs.index(c) == len(costs)-1):
                        bestBuild = build
                        break
                    pass
                else:
                    break
        else:
            break
    
    return bestBuild

def saveBuilds(builds, cps, baseCPS):
    with open("builds.txt","w") as file:
            for i in range(len(baseCPS)):
                file.write(str(builds[i]) + "," + str(cps[i]) + "\n")

def wipeBuilds(builds,cps,baseCPS,table):
    cps.clear()
    
    with open("text.txt","w") as file:
        for i in range(12):
            file.write("0," + baseCPS[i] + "\n")
            
    for b in builds:
        builds[builds.index(b)] = 0
        
    for c in baseCPS:
        try:
            cps.append(int(c))
        except:
            cps.append(float(c))
    
    i = -1
    for e in table:
        if (table.index(e) >= 5):
            if (table.index(e) % 5 == 1):
                #Count
                e.delete(0,tk.END)
                e.insert(0,builds[i])
            if (table.index(e) % 5 == 2):
                #CPS
                e.delete(0,tk.END)
                e.insert(0,cps[i])
            if (table.index(e) % 5 == 0):
                i+=1

def updateGrid(table,multi,builds: list,cps: list):
    variables = []
    builds.clear()
    cps.clear()
    
    i = 0
    for e in table:
        if (table.index(e) >= 5):
            if (table.index(e) % 5 == 1):
                #Count
                variables.append(int(e.get()))
                builds.append(int(e.get()))
                
            if (table.index(e) % 5 == 2):
                #CPS
                try:
                    variables.append(int(e.get()))
                    cps.append(int(e.get()))
                except:
                    variables.append(float(e.get()))
                    cps.append(float(e.get()))
            if (table.index(e) % 5 == 3):
                #Base Cost
                variables.append(int(e.get()))
                
            if (table.index(e) % 5 == 4):
                e.delete(0,tk.END)
                e.insert(0,round((variables[1]/(variables[2]*1.15**variables[0]))*multi, 3))

                variables.clear()

def main():
    steam = True
    
    # SETUP
    displayMultiplier = 100000
    baseCPS = ["0.1","1","8","47","260","1400","7800","44000","260000","1600000","10000000","65000000"]
    builds = []
    cps = []
    
    with open("builds.txt","r") as file:
        lines = file.readlines()
        for line in lines:
            builds.append(int(line.split(",")[0]))
            try:
                cps.append(int(line.split(",")[1].replace("\n","")))
            except:
                cps.append(float(line.split(",")[1].replace("\n","")))
            
    if (steam):
        buildingBox = box(1788,192,1864,1040)
        cookie = coord(290, 425)
        cursor = building("Cursor", coord(35,20), (92,98,94), (143,137,121), coord(1780,225), 15,0.1)
        grandma = building("Grandma", coord(35,85), (89,96,93), (138,132,116), coord(1780,285),100,1)
        farm = building("Farm", coord(35,150), (91,99,97), (138,135,120), coord(1780,350),1100,8)
        mine = building("Mine", coord(35,215), (106,112,107), (161,155,131), coord(1780, 415),12000,47)
        factory = building("Factory", coord(35,280), (100,107,105), (153,147,131), coord(1780,480),130000,260)
        bank = building("Bank", coord(35,345), (92,97,94), (141,134,118), coord(1780,540),1400000,1400)
        temple = building("Temple", coord(35,405), (90,99,97), (140,137,122), coord(1780,605),20000000,7800)
        wizard = building("Wizard Tower", coord(35,485), (103,113,108), (162,161,143), coord(1780, 675),330000000,44000)
        shipment = building("Shipment", coord(35,540), (90,98,95), (144,138,122), coord(1780,735),5100000000,260000)
        lab = building("Alchemy Lab", coord(35,605), (90,95,93), (143,138,119), coord(1780,800),75000000000,1600000)
        portal = building("Portal", coord(35,670), (94,102,100), (145,143,130), coord(1780,865),1000000000000,10000000)
        time = building("Time Machine", coord(35,720), (81,84,79), (131,126,11), coord(1780,0),14000000000000,65000000)
        upgrade = coord(1655,85)
        
    else:
        buildingBox = box(1788,305,1864,1040)
        cookie = coord(325, 485)
        cursor = building("Cursor", coord(35,20), (102,108,105), (158,152,136), coord(1780,330), 15,0.1)
        grandma = building("Grandma", coord(35,85), (91,98,96), (143,136,120), coord(1780,400),100,1)
        farm = building("Farm", coord(35,150), (94,102,100), (144,141,126), coord(1780,460),1100,8)
        mine = building("Mine", coord(35,215), (102,109,103), (159,153,131), coord(1780, 525),12000,47)
        factory = building("Factory", coord(35,280), (94,101,99), (145,139,123), coord(1780, 590),130000,260)
        bank = building("Bank", coord(35,345), (93,100,97), (144,136,121), coord(1780, 650),1400000,1400)
        temple = building("Temple", coord(35,405), (89,99,98), (141,138,123), coord(1780, 715),20000000,7800)
        wizard = building("Wizard Tower", coord(35,485), (101,109,103), (152,149,132), coord(1780, 780),330000000,44000)
        shipment = building("Shipment", coord(35,540), (99,107,103), (154,148,132), coord(1780,845),5100000000,260000)
        lab = building("Alchemy Lab", coord(35,605), (94,103,99), (143,138,119), coord(1780,910),75000000000,1600000)
        portal = building("Portal", coord(35,670), (93,102,100), (145,143,130), coord(1780,975),1000000000000,10000000)
        time = building("Time Machine", coord(35,720), (81,84,79), (131,126,11), coord(1780,1030),14000000000000,65000000)
        upgrade = coord(1655,195)
    
    running = False
    
    
    chromePos = [520,1060]
    mouse.move(chromePos[0],chromePos[1], 0.5)
    mouse.click()
    
    buildingArray = [cursor,grandma,farm,mine,factory,bank,temple,wizard,shipment,lab,portal,time]
    
    # GUI SETUP
    
    root = tk.Tk()
    root.wm_attributes("-topmost",1)
    root.geometry = ("500x500")

    topRow = ["Building", "Count", "CPS", "Base Cost", "Effectiveness"]
    tableEntries = []
    buildEntries = []
    effectivenessEntries = []
    cpsEntries = []
    prevBest = cursor

    for i in range(len(buildingArray)+1):
        for j in range(len(topRow)):
            e = tk.Entry(root, width=15, fg="black", font=("Arial",14,"bold"))
            if (i == 0):
                e.insert(0, topRow[j])
            elif (j == 0):
                e.insert(0, buildingArray[i-1].name)
            elif (j == 2):
                e.insert(0, cps[i-1])
                cpsEntries.append(e)
            elif (j == 1):
                e.insert(0, builds[i-1])
                buildEntries.append(e)
            elif (j == 3):
                e.insert(0,buildingArray[i-1].cost)
            elif (j == 4):
                effectivenessEntries.append(e)
                
            e.grid(row=i,column=j)
            tableEntries.append(e)       

    wipe = tk.Button(root, text="Wipe file", fg="white", bg="red", command = lambda: wipeBuilds(builds,cps,baseCPS,tableEntries), width=10,height=5)
    wipe.grid(row=len(builds)+1, column=0)
            
    update = tk.Button(root, text="Update", fg="white",bg="darkgray",width=15,height=5, command = lambda: updateGrid(tableEntries,displayMultiplier,builds,cps))
    update.grid(row=len(builds)+1,column=2)

    save = tk.Button(root, text="Save", fg="white", bg="red", command = lambda: saveBuilds(builds, cps, baseCPS), width=10,height=5)
    save.grid(row=len(builds)+1, column=len(topRow)-1)

    
    t.sleep(1)
    
    #MAIN LOOP INSIDE THE MSS
    
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
                    click(upgrade.x,upgrade.y, 5)
                    
                pic = sct.grab(buildings)
                
                if (pic.pixel(time.x,time.y) == time.color2 and (costCalc(builds,buildingArray,time,cps) or builds[11] == 0)):
                    click(time.tX,time.tY,1)
                    builds[11] += 1
                elif (pic.pixel(portal.x,portal.y) == portal.color2 and (costCalc(builds,buildingArray,portal,cps) or builds[10] == 0)):
                    click(portal.tX,portal.tY,1)
                    builds[10] += 1
                elif (pic.pixel(lab.x,lab.y) == lab.color2 and (costCalc(builds,buildingArray,lab,cps) or builds[9] == 0)):
                    click(lab.tX,lab.tY,1)
                    builds[9] += 1
                elif (pic.pixel(shipment.x,shipment.y) == shipment.color2 and (costCalc(builds,buildingArray,shipment,cps) or builds[8] == 0)):
                    click(shipment.tX,shipment.tY,1)
                    builds[8] += 1
                elif (pic.pixel(wizard.x,wizard.y) == wizard.color2 and (costCalc(builds,buildingArray,wizard,cps) or builds[7] == 0)):
                    click(wizard.tX,wizard.tY,1)
                    builds[7] += 1
                elif (pic.pixel(temple.x,temple.y) == temple.color2 and (costCalc(builds,buildingArray,temple,cps) or builds[6] == 0)):
                    click(temple.tX,temple.tY,1)
                    builds[6] += 1
                elif (pic.pixel(bank.x,bank.y) == bank.color2 and (costCalc(builds,buildingArray,bank,cps) or builds[5] == 0)):
                    click(bank.tX,bank.tY,1)
                    builds[5] += 1
                elif (pic.pixel(factory.x,factory.y) == factory.color2 and (costCalc(builds,buildingArray,factory,cps) or builds[4] == 0)):
                    click(factory.tX,factory.tY,1)
                    builds[4] += 1
                elif (pic.pixel(mine.x,mine.y) == mine.color2 and (costCalc(builds,buildingArray,mine,cps) or builds[3] == 0)):
                    click(mine.tX,mine.tY,1)
                    builds[3] += 1
                elif (pic.pixel(farm.x,farm.y) == farm.color2 and (costCalc(builds,buildingArray,farm,cps) or builds[2] == 0)):
                    click(farm.tX,farm.tY,1)
                    builds[2] += 1
                elif (pic.pixel(grandma.x,grandma.y) == grandma.color2 and (costCalc(builds,buildingArray,grandma,cps) or builds[1] == 0)):
                    click(grandma.tX,grandma.tY,1)
                    builds[1] += 1
                elif (pic.pixel(cursor.x,cursor.y) == cursor.color2 and (costCalc(builds,buildingArray,cursor,cps) or builds[0] == 0)):
                    click(cursor.tX,cursor.tY,1)
                    builds[0] += 1
                    
                running = click(cookie.x,cookie.y, 100)
            
            
            root.update_idletasks()
            root.update()
            
            for e in buildEntries:
                e.delete(0,tk.END)
                e.insert(0,builds[buildEntries.index(e)])
                
            for c in cpsEntries:
                if (c.get() != ""):
                    try:
                        cps[cpsEntries.index(c)] = int(c.get())
                    except:
                        cps[cpsEntries.index(c)] = float(c.get())
                        
            best = calcAllCosts(builds,buildingArray,cps)
            if (prevBest != best):
                effectivenessEntries[buildingArray.index(best)].config({"bg":"#93E9BE"})
                effectivenessEntries[buildingArray.index(prevBest)].config({"bg":"white"}) 
                prevBest = best
            else:
                pass
            updateGrid(tableEntries,displayMultiplier,builds,cps)
                
        saveBuilds(builds,cps,baseCPS)
                
    
if __name__ == "__main__":
    main()