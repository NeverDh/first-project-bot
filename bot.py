from ast import Continue
from platform import python_branch
from sre_constants import REPEAT
from tkinter import PhotoImage
from xmlrpc.client import boolean
import cv2
from cv2 import repeat
from matplotlib import image
from numpy import true_divide
import pyautogui
import pyscreenshot as ImageGrab
import time
from PIL import Image

screenWidth, screenHeight = pyautogui.size()

time.sleep(1)

def loggin():

    connectPos = pyautogui.locateCenterOnScreen("alvos/Conectar.png")
    pyautogui.click(connectPos.x, connectPos.y, duration=0.5)

    time.sleep(2)

    connectPosTwo = pyautogui.locateCenterOnScreen("alvos/ConectarTwo.png", confidence=0.9)
    pyautogui.click(connectPosTwo.x, connectPosTwo.y, duration=0.5)

    time.sleep(6)

    connectMetaPos = pyautogui.locateCenterOnScreen("alvos/conectar_metamask.png")
    pyautogui.click(connectMetaPos.x, connectMetaPos.y, duration=0.5)

    time.sleep(15)
    heroes()



def farm():

    time.sleep(3)
    farmPos = pyautogui.locateCenterOnScreen("alvos/farmar.png")
    pyautogui.click(farmPos.x, farmPos.y, duration=0.5)
    time.sleep(600)
    quitFarm()



def quitFarm():

    quitFarmPos = pyautogui.locateCenterOnScreen("alvos/sair_farm.png")
    quitFarmPosTwo = pyautogui.locateCenterOnScreen("alvos/sair_farmTwo.png")

    if quitFarmPos != None:
        pyautogui.click(quitFarmPos.x, quitFarmPos.y, duration=0.5)
    elif quitFarmPosTwo != None:
        pyautogui.click(quitFarmPosTwo.x, quitFarmPosTwo.y, duration=0.5) 
    time.sleep(1)
    refresh()



def heroes():

    heroesPos = pyautogui.locateCenterOnScreen("alvos/herois.png", confidence=0.9)
    pyautogui.click(heroesPos.x, heroesPos.y, duration=0.5)
    time.sleep(3)
    locSelHeroes()



def quitHeroes():

    time.sleep(2)
    quitHeroesPos = pyautogui.locateCenterOnScreen("alvos/sair_herois.png")
    quitHeroesPosTwo = pyautogui.locateCenterOnScreen("alvos/sair_heroisTwo.png")
    quitHeroesPosThree = pyautogui.locateCenterOnScreen("alvos/sair_heroisThree.png")

    if quitHeroesPos != None:
        pyautogui.click(quitHeroesPos.x, quitHeroesPos.y, duration=1)

    elif quitHeroesPosTwo != None:
        pyautogui.click(quitHeroesPosTwo.x, quitHeroesPosTwo.y, duration=0.5)
    else:
        pyautogui.click(quitHeroesPosThree.x, quitHeroesPosThree.y, duration=0.5)

    time.sleep(2)
    farm()



def locSelHeroes():

    staminaPos = pyautogui.locateCenterOnScreen("alvos/stamina.png", confidence=0.9)

    if staminaPos != None: 
        SelHeroes(staminaPos, i=0)
    else:
        rolHeroes()

    

def SelHeroes(staminaPos, i):
    
    if staminaPos != None:
        for pos in pyautogui.locateAllOnScreen("alvos/stamina.png"):
            x = pos.left
            y = pos.top

            if i >= 1:
                workPos = Image.open("alvos/workLow1.png")
                workPosTwo = Image.open("alvos/workLowTwo1.png")
                pyautogui.screenshot("work1.png", region=(x+125, y-15, 60, 40))
                pyautogui.screenshot("workTwo1.png", region=(x+121, y-20, 65, 50))

                teste = Image.open("work1.png")
                teste2 = Image.open("workTwo1.png")

                if workPos == teste:
                    pyautogui.click(x+150, y, duration=1)
                elif workPosTwo == teste2: 
                    pyautogui.click(x+150, y, duration=1)
                else:  
                    continue
            else:
                workPos = Image.open("alvos/work1.png")
                workPosTwo = Image.open("alvos/workTwo1.png")
                pyautogui.screenshot("work1.png", region=(x+125, y-15, 60, 40))
                pyautogui.screenshot("workTwo1.png", region=(x+121, y-20, 65, 50))

                teste = Image.open("work1.png")
                teste2 = Image.open("workTwo1.png")

                if workPos == teste:
                    pyautogui.click(x+150, y, duration=1.5)
                elif workPosTwo == teste2: 
                    pyautogui.click(x+150, y, duration=1.5)
                else:  
                    continue

    time.sleep(1)

    
    rolHeroes(i)
    
    

def rolHeroes(i):

    positionOn = pyautogui.locateCenterOnScreen("alvos/work_selecionado.png")
    positionOnTwo = pyautogui.locateCenterOnScreen("alvos/work_selecionadoTwo.png")
    if positionOn != None:
        pyautogui.moveTo(positionOn.x, positionOn.y)
        pyautogui.dragTo(positionOn.x, positionOn.y-250, duration=0.5)
    elif positionOnTwo != None: 
        pyautogui.moveTo(positionOnTwo.x, positionOnTwo.y)
        pyautogui.dragTo(positionOnTwo.x, positionOnTwo.y-250, duration=0.5)

    time.sleep(2)

    staminaPos = pyautogui.locateCenterOnScreen("alvos/stamina.png", confidence=0.9)
    if staminaPos != None:
        i = i+1
        if i >= 3:
            quitHeroes()
        else:
            SelHeroes(staminaPos, i)



def refresh():

    pyautogui.hotkey('ctrlleft', 'f5')
    time.sleep(20)
    loggin()



def identify():

    time.sleep(3)

    connectPos = pyautogui.locateCenterOnScreen("alvos/Conectar.png", confidence=0.9)
    heroesPos = pyautogui.locateCenterOnScreen("alvos/herois.png", confidence=0.9)
    workPos = pyautogui.locateCenterOnScreen("alvos/work1.png", confidence=0.9)
    workPos2 = pyautogui.locateCenterOnScreen("alvos/workTwo1.png", confidence=0.9)
    quitFarmPos = pyautogui.locateCenterOnScreen("alvos/sair_farm.png", confidence=0.9)
    positionOn = pyautogui.locateCenterOnScreen("alvos/work_selecionado.png", confidence=0.9)
    positionOnTwo = pyautogui.locateCenterOnScreen("alvos/work_selecionadoTwo.png", confidence=0.9)

    if connectPos != None:
        loggin()
    elif heroesPos != None:
        heroes()
    elif workPos != None or workPos2 != None or positionOn != None or positionOnTwo != None:
        locSelHeroes()
    elif quitFarmPos != None:
        quitFarm()





    

#loggin()
#farm()
#quitFarm()
#heroes()
#locSelHeroes()
#staminaHeroes()
#refresh()
#quitHeroes()
identify()


            







