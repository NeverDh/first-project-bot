from platform import python_branch
from xmlrpc.client import boolean
import cv2
from numpy import true_divide
import pyautogui
import pyscreenshot as ImageGrab
import time
from PIL import Image

screenWidth, screenHeight = pyautogui.size()

time.sleep(1)

def loggin():

    connectPos = pyautogui.locateCenterOnScreen("alvos/Conectar.png")
    pyautogui.click(connectPos.x, connectPos.y)

    time.sleep(6)

    connectMetaPos = pyautogui.locateCenterOnScreen("alvos/conectar_metamask.png")
    pyautogui.click(connectMetaPos.x, connectMetaPos.y)

    time.sleep(15)
    heroes()



def farm():

    time.sleep(3)
    farmPos = pyautogui.locateCenterOnScreen("alvos/farmar.png")
    pyautogui.click(farmPos.x, farmPos.y, duration=1)
    time.sleep(600)
    quitFarm()



def quitFarm():

    quitFarmPos = pyautogui.locateCenterOnScreen("alvos/sair_farm.png")
    quitFarmPosTwo = pyautogui.locateCenterOnScreen("alvos/sair_farmTwo.png")

    if quitFarmPos != None:
        pyautogui.click(quitFarmPos.x, quitFarmPos.y)
    elif quitFarmPosTwo != None:
        pyautogui.click(quitFarmPosTwo.x, quitFarmPosTwo.y) 
    time.sleep(1)
    refresh()



def heroes():

    heroesPos = pyautogui.locateCenterOnScreen("alvos/herois.png")
    pyautogui.click(heroesPos.x, heroesPos.y)
    time.sleep(3)
    locSelHeroes()



def quitHeroes():

    time.sleep(2)
    quitHeroesPos = pyautogui.locateCenterOnScreen("alvos/sair_herois.png")
    quitHeroesPosTwo = pyautogui.locateCenterOnScreen("alvos/sair_heroisTwo.png")
    quitHeroesPosThree = pyautogui.locateCenterOnScreen("alvos/sair_heroisThree.png")

    if quitHeroesPos != None:
        pyautogui.click(quitHeroesPos.x, quitHeroesPos.y)

    elif quitHeroesPosTwo != None:
        pyautogui.click(quitHeroesPosTwo.x, quitHeroesPosTwo.y)
    else:
        pyautogui.click(quitHeroesPosThree.x, quitHeroesPosThree.y)

    time.sleep(2)
    farm()



def locSelHeroes():

    workPos = pyautogui.locateCenterOnScreen("alvos/work.png")
    workPos2 = pyautogui.locateCenterOnScreen("alvos/workTwo.png")
    if workPos != None or workPos2 != None:
        SelHeroes()
    else:
        rolHeroes()



def SelHeroes():
    
    workPos = pyautogui.locateCenterOnScreen("alvos/work.png")
    workPos2 = pyautogui.locateCenterOnScreen("alvos/workTwo.png")
    if workPos != None:
        pyautogui.click(workPos.x, workPos.y)
        time.sleep(1)
        locSelHeroes()
    else:
        pyautogui.click(workPos2.x, workPos2.y)
        time.sleep(1)
        locSelHeroes()



def rolHeroes():

    positionOn = pyautogui.locateCenterOnScreen("alvos/work_selecionado.png")
    positionOnTwo = pyautogui.locateCenterOnScreen("alvos/work_selecionadoTwo.png")
    if positionOn != None:
        pyautogui.moveTo(positionOn.x, positionOn.y)
        pyautogui.dragTo(positionOn.x, positionOn.y-250, duration=1)
    elif positionOnTwo != None: 
        pyautogui.moveTo(positionOnTwo.x, positionOnTwo.y)
        pyautogui.dragTo(positionOnTwo.x, positionOnTwo.y-250, duration=1)
    time.sleep(2)
    position = pyautogui.locateCenterOnScreen("alvos/work.png")
    position2 = pyautogui.locateCenterOnScreen("alvos/workTwo.png")
    if position != None or position2 != None:
        SelHeroes()
    else:
        quitHeroes()



def refresh():

    pyautogui.hotkey('ctrlleft', 'f5')
    time.sleep(20)
    loggin()



def identify():

    time.sleep(5)

    connectPos = pyautogui.locateCenterOnScreen("alvos/Conectar.png")
    heroesPos = pyautogui.locateCenterOnScreen("alvos/herois.png")
    workPos = pyautogui.locateCenterOnScreen("alvos/work.png")
    workPos2 = pyautogui.locateCenterOnScreen("alvos/workTwo.png")
    quitFarmPos = pyautogui.locateCenterOnScreen("alvos/sair_farm.png")
    positionOn = pyautogui.locateCenterOnScreen("alvos/work_selecionado.png")
    positionOnTwo = pyautogui.locateCenterOnScreen("alvos/work_selecionadoTwo.png")

    if connectPos != None:
        loggin()
    elif heroesPos != None:
        heroes()
    elif workPos != None or workPos2 != None or positionOn != None or positionOnTwo != None:
        locSelHeroes()
    else:
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






