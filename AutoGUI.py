import cv2
from time import sleep
import numpy as np
import pyautogui as gui
import pydirectinput as dp
from MatchTool import ImageMatch
gui.FAILSAFE=False

def Get_Scene():
    image = gui.screenshot()
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    return image

def Desktop():
    gui.hotkey('win', 'd')

def Get_Object(obj):
    template = cv2.imread(obj)
    target = Get_Scene()
    min_loc, width, height, val = ImageMatch(target, template)
    dp.moveTo(int(min_loc[0]+width/2), int(min_loc[1]+height/2), 0.1)
    print(int(min_loc[0]+width/2), int(min_loc[1]+height/2))
    if np.abs(val) > 1e-10:
        return False
    else:
        return True

def LeftClick():
    dp.leftClick()

def Open():
    dp.doubleClick()

if __name__=='__main__':
    sleep(2)
    dp.moveTo(1441,824)