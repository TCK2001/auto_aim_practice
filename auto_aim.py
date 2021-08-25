import pyautogui as pag 
from PIL import ImageGrab 
import keyboard 
SB=1 
shot=0 
start=(305, 174)
end=(1614, 979)
c_bull=(131, 147, 171)

while SB==1:
    screen = ImageGrab.grab() 
    for i in range(start[0],end[0],10):
        for j in range(start[1],end[1],10):
            rgb=screen.getpixel((i,j)) 
            if abs(rgb[0]-c_bull[0])+abs(rgb[1]-c_bull[1])+abs(rgb[2]-c_bull[2])<50: 
                rgb=screen.getpixel((i+3,j)) 
                if abs(rgb[0]-c_bull[0])+abs(rgb[1]-c_bull[1])+abs(rgb[2]-c_bull[2])<25:
                    pag.click((i+3,j))
                    shot=1
                    break
        if shot==1: 
            shot=0
            break
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
#         screen = ImageGrab.grab() 
#         print(screen.getpixel(pag.position()))
#     if keyboard.is_pressed('F3'):
#         SB=0
#         break 
