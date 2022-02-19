import cv2
import pyautogui
import pyscreenshot as ImageGrab
import time

screenWidth, screenHeight = pyautogui.size()

time.sleep(1)

herosPos = pyautogui.locateCenterOnScreen("alvos/herois.png")

print(herosPos)

farmPos = pyautogui.locateCenterOnScreen("alvos/farmar.png")

print(herosPos)

workPos = pyautogui.locateCenterOnScreen("alvos/work.png")

print(herosPos)

resPos = pyautogui.locateCenterOnScreen("alvos/rest.png")

print(herosPos)

workSelPos = pyautogui.locateCenterOnScreen("alvos/work_selecionado.png")

print(herosPos)

restSelPos = pyautogui.locateCenterOnScreen("alvos/rest_selecionado.png")

print(herosPos)

quitHerPos = pyautogui.locateCenterOnScreen("alvos/sair_herois.png")

print(herosPos)

quitFarmPos = pyautogui.locateCenterOnScreen("alvos/sair_farm.png")

print(herosPos)

connectPos = pyautogui.locateCenterOnScreen("alvos/Conectar.png")

print(herosPos)

connectMetaPos = pyautogui.locateCenterOnScreen("alvos/conectar_metamask.png")

print(herosPos)







