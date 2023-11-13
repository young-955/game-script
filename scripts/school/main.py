import torch
import numpy as np
import os
from libs.find_item import get_screenshot
from config import *

# 获取当前脚本所在的目录
current_dir = os.path.dirname(os.path.abspath(__file__))
# 将执行路径设置为项目的最上级目录
project_root = os.path.abspath(os.path.join(current_dir, ".."))

def main():
    # get screen
    img = get_screenshot(SCHOOL)

    
