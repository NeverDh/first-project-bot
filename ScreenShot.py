import pyscreenshot as ImageGrab
import pyautogui

def main():
    im = pyautogui.screenshot(region=(0,0, 300, 400))
    im.save('screenShot.jpg', 'jpeg')

if __name__ == "__main__":
    main()