import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import tool.AutoGUI as g
from time import sleep
from tool.Logger import logger

LOGO = 'bin\\logo.png'
SHOTCUT = 'bin\\shotcut.png'
START = 'bin\\start.png'
TITLE = 'bin\\title.png'
ENTER = 'bin\\enter.png'
OK = 'bin\\ok.png'
PHONE = 'bin\\phone.png'
INSTANCE_ON = 'bin\\instance_on.png'
INSTANCE_OFF = 'bin\\instance_off.png'
GOLD_OFF = 'bin\\gold_off.png'
GOLD_ON = 'bin\\gold_on.png'

def Openning():
    """判断《崩坏：星穹铁道》是否运行?"""
    logger.info("【判断】《崩坏：星穹铁道》是否开启：")
    g.Get_Scene()
    if g.Get_Object(LOGO):
        logger.info("【结果】已开启。")
        return True
    else:
        logger.warning("【结果】未开启。")
        return False

def Uncovering():
    """判断《崩坏：星穹铁道》是否显示"""
    if not Openning():
        return False
    else:
        logger.info("【判断】《崩坏：星穹铁道》是否显示在上方：")
        if g.Get_Object(START):
            logger.info('【结果】处于启动器界面。')
        elif g.Get_Object(TITLE):
            logger.info('【结果】已进入游戏。')
        else:
            logger.warning('【结果】未显示')
            return False
        return True      

def Open_StarRail():
    """运行《崩坏：星穹铁道》"""
    if Openning():
        logger.info('《崩坏：星穹铁道》正在运行')
    else:
        g.Desktop()
        sleep(1)
        g.Get_Object(SHOTCUT)
        g.Open()
        if g.Wait_Until({LOGO}):
            logger.info('《崩坏：星穹铁道》已打开')
        else:
            logger.warning('打开异常，请联系管理员')

def Uncover_StarRail():
    """显示《崩坏：星穹铁道》"""
    if not Uncovering():
        # 点击任务栏图标
        logger.info("【操作】点击任务栏图标")
        g.hide_mouse()
        g.sleep(1)
        if g.Get_Object(LOGO):
            g.LeftClick()
            g.hide_mouse()
        # 等待结果
        logger.info("【等待】完成操作,监测屏幕中。。。")
        if g.Wait_Until({TITLE}):
            logger.info('【结果】监测到窗口标题，操作完成。')
            return True
        else:
            logger.warning('【异常】未监测到窗体标题，异常！')
            return False
    return False

def Start_StarRail():
    """开始游戏"""
    g.hide_mouse()
    logger.info("【操作】点击“进入游戏”按钮")
    if g.Get_Object(START):
        g.LeftClick()
        g.hide_mouse()
    # 等待结果
    logger.info("【等待】完成操作,监测屏幕中。。。")
    if g.Wait_Until({ENTER}):
        logger.info('【结果】监测到窗口标题，操作完成。')
        return True
    else:
        logger.warning('【异常】未监测到进入游戏按钮""，异常！')
        return False   

def Enter_StarRail():
    g.hide_mouse()
    logger.info("【操作】点击“进入游戏”按钮")
    if g.Get_Object(ENTER):
        g.LeftClick()
        logger.info("【等待】操作完成，监测屏幕中")
    else:
        logger.info("【异常】无法定位“进入游戏”按钮")
    if g.Wait_Until({PHONE}):
        logger.info("【结果】监测到“手机”按钮，已进入游戏")
        return True
    else:
        logger.warning("【结果】未监测到“手机”按钮，异常")
        return False

def Ok():
    g.hide_mouse()
    g.Get_Object(OK)
    g.LeftClick()

def Phone():
    g.Call_Mouse()
    g.Get_Object(PHONE)
    g.LeftClick()
    g.Release_Mouse()

def Guidence():
    g.Click_Key('f4')
    if g.Wait_Until({INSTANCE_ON, INSTANCE_OFF}):
        return True
    else:
        return False

def Instance():
    g.hide_mouse()
    if g.Get_Object(INSTANCE_OFF):
        g.LeftClick()
    if g.Wait_Until({INSTANCE_ON}):
        return True
    else:
        return False
    

def Gold():
    if g.Get_Object(INSTANCE_OFF):
        g.LeftClick()


if __name__=='__main__':
    Open_StarRail()