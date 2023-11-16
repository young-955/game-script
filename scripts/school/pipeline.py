import torch
import numpy as np
from loguru import logger
import time
import os
import sys
# 获取当前脚本所在的目录
current_dir = os.path.dirname(os.path.abspath(__file__))
# 将执行路径设置为项目的最上级目录
project_root = os.path.abspath(os.path.join(current_dir, "../../"))
sys.path.append(project_root)

from models.infer.rapid_ocr import ocr_area
from libs.school.entrance import enter_game
from config import *


appname = "全民学霸"
# 小程序区域
# (715,50) (1200, 50) (715, 980) (1200, 980)
# screenshot 参数xy+宽高
region = (715, 50, 485, 930)

def pipeline(res):
    # 进入主页面
    enter_finished = enter_game(res, region)
    if not enter_finished:
        logger.info("enter failed")
        return

    return 

def main():
    time.sleep(5)
    res = ocr_area(game_id=SCHOOL, region=region, debug=debug)

    # 检测是否包含目标小程序
    flag = False
    for data in res:
        if appname in data[1]:
            flag = True
            break
        else:
            logger.info("appname not found")
    
    # 执行流程
    if flag:
        pipeline(res)
