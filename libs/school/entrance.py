import os
import sys
# 获取当前脚本所在的目录
current_dir = os.path.dirname(os.path.abspath(__file__))
# 将执行路径设置为项目的最上级目录
project_root = os.path.abspath(os.path.join(current_dir, "../../"))
sys.path.append(project_root)

from libs.system_func import safe_mouse_click, safe_mouse_drag

def enter_game(res, region):
    offsetx = 0
    offsety = 0

    # 处理公告和校刊界面，正常应该不会出现校刊界面，暂时注释
    close_notice(res, region)
    # close_magazine(res, region)
    for data in res:
        if "开始游戏" in data[1]:
            for xy in data[0]:
                offsetx += xy[0]
                offsety += xy[1]
            
            offsetx /= 4
            offsety /= 4

            safe_mouse_click(region[0] + offsetx, region[1] + offsety, wait=1)

            return True

    return False

def close_notice(res, region):
    offsetx = 0
    offsety = 0
    notice_flag = False
    notice_flag2 = False
    for data in res:
        if "游戏公告" in data[1]:
            notice_flag = True
            if notice_flag2:
                break
        if "知道了" in data[1]:
            for xy in data[0]:
                offsetx += xy[0]
                offsety += xy[1]
            offsetx /= 4
            offsety /= 4
            notice_flag2 = True
            if notice_flag:
                break

    if notice_flag:
        safe_mouse_click(region[0] + offsetx, region[1] + offsety, wait=1)

def close_magazine(res, region):
    offsetx = 0
    offsety = 0

    for data in res:
        if "上一篇" in data[1]:
            for xy in data[0]:
                offsetx += xy[0]
                offsety += xy[1]
            offsetx /= 4
            offsety /= 4

            # TODO 校刊有点难搞，写死
            safe_mouse_click(1167, 246, wait=1)
            close_notice(res, region)

            break
