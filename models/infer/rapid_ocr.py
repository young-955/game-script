from rapidocr_onnxruntime import RapidOCR
import os
import sys
import time
# 获取当前脚本所在的目录
current_dir = os.path.dirname(os.path.abspath(__file__))
# 将执行路径设置为项目的最上级目录
project_root = os.path.abspath(os.path.join(current_dir, "../../"))
sys.path.append(project_root)

from libs import system_func
from config import SCHOOL, debug

engine = RapidOCR()

def demo():
    time.sleep(5)
    img = system_func.get_screenshot(region=(715, 50, 485, 930))
    result, elapse = engine(img)
    # print(type(result))
    # print(type(result[0]))
    print(result[0][1])
    print(result)

def ocr_area(game_id = SCHOOL, region = ()):
    img = system_func.get_screenshot(game_id=game_id, region=region)
    if debug:
        img.save('./screenshot.jpg')
    result, elapse = engine(img)

    return result

if __name__ == "__main__":
    demo()