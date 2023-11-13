import pyautogui
import cv2
import numpy as np
import os

# 获取当前脚本所在的目录
current_dir = os.path.dirname(os.path.abspath(__file__))
# 将执行路径设置为项目的最上级目录
project_root = os.path.abspath(os.path.join(current_dir, ".."))

os.chdir(project_root)
def get_screenshot(game_id):
    # 获取屏幕截图
    screenshot = pyautogui.screenshot()

    # # 保存截图为文件
    # screenshot.save('./resources/screenshot.png')
    return cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

def get_screenshot():
    # 读取截图
    image = cv2.imread('screenshot.png')

    # 进行图像处理，例如颜色过滤
    # ...

    # 显示处理后的图像
    cv2.imshow('Processed Image', processed_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

