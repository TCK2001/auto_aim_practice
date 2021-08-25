import pyautogui as pag
from PIL import ImageGrab
import keyboard
import time

SB=1
point=(924, 574)
bull=(97, 113, 140)
# bg=(226, 235, 250)
while SB==1:
    screen=ImageGrab.grab()
    rgb=screen.getpixel(point)
    # print(rgb)
    if abs(rgb[0]-bull[0])+abs(rgb[1]-bull[1])+abs(rgb[2]-bull[2])<50:
        pag.click(point)
        time.sleep(1)
    if keyboard.is_pressed('F3'):
        SB=0
        break


# SB=0
# while SB==0:
#     if keyboard.is_pressed('F4'):
#         x, y = pag.position()
#         print((x,y))
#     if keyboard.is_pressed('F3'):
#         SB=0
#         break 




# SB=0
# while SB==0:
#     if keyboard.is_pressed('F4'):
#         screen = ImageGrab.grab() # 화면 캡쳐
#         print(screen.getpixel(pag.position()))
#     if keyboard.is_pressed('F3'):
#         SB=0
#         break 