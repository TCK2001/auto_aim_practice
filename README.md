## auto_aim_practice
------
```
https://aim400kg.com 
```
+  This is test code sites.
------
+ First code is Accuracy.
+ Second code is Quickness.
+ Third code is Reflex.
```python
import pyautogui as pag 
from PIL import ImageGrab 
import keyboard
```
* We will use pyautogui to coding.
```python
if abs(rgb[0]-c_bull[0])+abs(rgb[1]-c_bull[1])+abs(rgb[2]-c_bull[2])<50: 
    rgb=screen.getpixel((i+3,j)) 
        if abs(rgb[0]-c_bull[0])+abs(rgb[1]-c_bull[1])+abs(rgb[2]-c_bull[2])<25:
            pag.click((i+3,j))....
```
+ When the ball gets smaller,we have to i+3 to prevent it from being clicked.
------
+ The code is Easy but the important things is you have to check the upper left and lower right coordinates.
```python
SB=0
while SB==0:
    if keyboard.is_pressed('F4'):
        x, y = pag.position()
        print((x,y))
    if keyboard.is_pressed('F3'):
        SB=0
        break #Use this program to find the upper left and lower right coordinates.
```
------
```python
SB=0
while SB==0:
    if keyboard.is_pressed('F4'):
        screen = ImageGrab.grab() 
        print(screen.getpixel(pag.position()))
    if keyboard.is_pressed('F3'):
        SB=0
        break #Use this program to find the ball color.
```
