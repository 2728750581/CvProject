import os
import AutoGUI as g
from time import sleep

LOGO = 'bin\\logo.png'
SHOTCUT = 'bin\\shotcut.png'
START = 'bin\\start.png'
TITLE = 'bin\\title.png'


def Openning():
    """判断《崩坏：星穹铁道》是否运行?"""
    g.Get_Scene()
    return g.Get_Object(LOGO)


def Uncovering():
    """判断《崩坏：星穹铁道》是否显示"""
    if not Openning():
        print('《崩坏：星穹铁道》未打开')
        return False
    else:
        if g.Get_Object(START):
            print('《崩坏：星穹铁道》处于启动器界面')
        elif g.Get_Object(TITLE):
            print('《崩坏：星穹铁道》已进入游戏')
        else:
            print('《崩坏：星穹铁道》未显示')
            return False
        return True
        

def Open_StarRail():
    """运行《崩坏：星穹铁道》"""
    if Openning():
        print('《崩坏：星穹铁道》正在运行')
    else:
        g.Desktop()
        sleep(1)
        g.Get_Object(SHOTCUT)
        g.Open()
        sleep(2)
        # if Openning():
        #     print('《崩坏：星穹铁道》已打开')
        #     print('《崩坏：星穹铁道》正在运行')
        # else:
        #     print('打开异常，请联系管理员')


def Uncover_StarRail():
    """显示《崩坏：星穹铁道》"""
    if Openning() and not Uncovering():
        g.Get_Object(LOGO)
        g.LeftClick()
        if Uncovering():
            print('《崩坏：星穹铁道》显示在上方')
            return True
        else:
            print('显示异常，请联系管理员')
            return False


def Start_StarRail():
    """进入游戏"""
    g.Get_Object(START)
    g.LeftClick()


def Login_StarRail():
    """登录游戏"""
    pass

Open_StarRail()
#Uncover_StarRail()
#Start_StarRail()