import pyautogui as pag # 마우스 제어
from PIL import ImageGrab # 화면 캡쳐
import keyboard 
SB=1 # 종료키 기능을 위한 변수
shot=0 # 목표물 찾았는지 확인하는 변수
start=(305, 174)
end=(1614, 979)
c_bull=(131, 147, 171)

while SB==1:
    screen = ImageGrab.grab() # 화면 캡쳐
    for i in range(start[0],end[0],10):
        for j in range(start[1],end[1],10):
            rgb=screen.getpixel((i,j)) # 각 좌표에서의 rgb값 추출
            if abs(rgb[0]-c_bull[0])+abs(rgb[1]-c_bull[1])+abs(rgb[2]-c_bull[2])<50: 
                rgb=screen.getpixel((i+3,j)) # (i+3,j)에서 rgb값 추출
                if abs(rgb[0]-c_bull[0])+abs(rgb[1]-c_bull[1])+abs(rgb[2]-c_bull[2])<25:
                    pag.click((i+3,j))
                    shot=1
                    break
        if shot==1: # 목표물 찾았다면 for문 빠져나옴
            shot=0
            break
    if keyboard.is_pressed('F3'): # 코드 종료
        SB=0
        break 


# x, y = pag.position()
# print((x,y))


# SB=0
# while SB==0:
#     if keyboard.is_pressed('F4'):
#         screen = ImageGrab.grab() # 화면 캡쳐
#         print(screen.getpixel(pag.position()))
#     if keyboard.is_pressed('F3'):
#         SB=0
#         break 