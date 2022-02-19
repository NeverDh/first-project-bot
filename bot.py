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

    time.sleep(5)

    connectMetaPos = pyautogui.locateCenterOnScreen("alvos/conectar_metamask.png")
    pyautogui.click(connectMetaPos.x, connectMetaPos.y)

    time.sleep(5)



def farm():

    farmPos = pyautogui.locateCenterOnScreen("alvos/farmar.png")
    pyautogui.click(farmPos.x, farmPos.y)
    time.sleep(1)



def quitFarm():

    quitFarmPos = pyautogui.locateCenterOnScreen("alvos/sair_farm.png")
    pyautogui.click(quitFarmPos.x, quitFarmPos.y)
    time.sleep(1)



def heroes():

    heroesPos = pyautogui.locateCenterOnScreen("alvos/herois.png")
    pyautogui.click(heroesPos.x, heroesPos.y)
    time.sleep(3)



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
    if positionOn != None:
        pyautogui.moveTo(positionOn.x, positionOn.y)
        pyautogui.dragTo(positionOn.x, positionOn.y-200, duration=1)
        time.sleep(3)
        position = pyautogui.locateCenterOnScreen("alvos/work.png")
        position2 = pyautogui.locateCenterOnScreen("alvos/workTwo.png")
        if position != None or position2 != None:
            SelHeroes()
        else:
            quit()
 
            

#loggin()
#farm()
#quitFarm()
#heroes()
locSelHeroes()
#staminaHeroes()



