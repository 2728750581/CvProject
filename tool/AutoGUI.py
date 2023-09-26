import cv2
from time import sleep
import numpy as np
import pyautogui as gui
import pydirectinput as dp
from tool.MatchTool import ImageMatch
gui.FAILSAFE=False

def hide_mouse():
    width, height = gui.size()
    dp.moveTo(width, height, 0.1)

def Get_Scene():
    image = gui.screenshot()
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    return image

def Store_Scene():
    image = gui.screenshot()
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    cv2.imwrite("..\\qsign-onekey-1.1.9-fix1\\data\\images\\scene.png", image)
    return True

def Desktop():
    gui.hotkey('win', 'd')

def Get_Object(obj):
    template = cv2.imread(obj)
    target = Get_Scene()
    min_loc, width, height, val = ImageMatch(target, template)
    dp.moveTo(int(min_loc[0]+width/2), int(min_loc[1]+height/2), 0.3)
    if np.abs(val) > 1e-10:
        return False
    else:
        return True

def LeftClick():
    dp.leftClick()

def Open():
    dp.doubleClick()

def Wait_Until(objs, inter_time=1, max_inter=30):
    i = 0
    while i < max_inter:
        i = i+1
        for obj in objs:
            if Get_Object(obj):
                return True
        sleep(inter_time)
        
    return False

def Call_Mouse():
    dp.keyDown('alt')

def Release_Mouse():
    dp.keyUp('alt')

def Click_Key(key):
    dp.keyDown(key)
    dp.keyUp(key)

if __name__=='__main__':
    Store_Scene()