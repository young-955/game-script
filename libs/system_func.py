import os
import pyautogui
import cv2
import numpy as np
import time
from config import SCHOOL


def get_screenshot(game_id = SCHOOL, region = ()):
    # 获取屏幕截图
    if region == ():
        screenshot = pyautogui.screenshot()
    else:
        screenshot = pyautogui.screenshot(region=region)

    # # 保存截图为文件
    # screenshot.save('./resources/screenshot.png')
    return cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

def safe_mouse_click(x, y, button='left', clicks=1, interval=0.1, wait=0.5):
    """
    参数：
    - x, y: 点击的坐标位置
    - button: 鼠标按钮，'left' 或 'right'
    - clicks: 点击次数
    - interval: 点击间隔时间（秒）
    - wait: 点击后缓冲等待时间

    返回：
    - True: 点击成功
    - False: 点击失败
    """
    try:
        # 移动鼠标到目标位置
        pyautogui.moveTo(x, y, duration=0.25)

        # 模拟点击
        pyautogui.click(x=x, y=y, button=button, clicks=clicks, interval=interval)

        # 等待点击完成
        time.sleep(wait)

        return True
    except pyautogui.FailSafeException:
        # pyautogui.FailSafeException 表示鼠标移动到屏幕角落触发的异常
        print("安全模式触发，脚本终止")
        return False
    except Exception as e:
        # 处理其他可能的异常
        print(f"点击失败：{e}")
        return False
    
def safe_mouse_drag(start_x, start_y, end_x, end_y, duration=1.0, wait=0.5):
    """
    安全的鼠标左键拖动函数，考虑了异常情况

    参数：
    - start_x, start_y: 拖动起始位置的坐标
    - end_x, end_y: 拖动结束位置的坐标
    - duration: 拖动持续时间（秒）
    - wait: 点击后缓冲等待时间

    返回：
    - True: 拖动成功
    - False: 拖动失败
    """
    try:
        # 移动鼠标到起始位置
        pyautogui.moveTo(start_x, start_y, duration=0.25)

        # 鼠标按下
        pyautogui.mouseDown()

        # 拖动至结束位置
        pyautogui.moveTo(end_x, end_y, duration=duration)

        # 鼠标释放
        pyautogui.mouseUp()

        # 等待动作完成
        time.sleep(wait)

        return True
    except pyautogui.FailSafeException:
        # pyautogui.FailSafeException 表示鼠标移动到屏幕角落触发的异常
        print("安全模式触发，脚本终止")
        return False
    except Exception as e:
        # 处理其他可能的异常
        print(f"拖动失败：{e}")
        return False