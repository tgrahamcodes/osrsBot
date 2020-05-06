import pyautogui
import time
import random

brown = [] 

def go(x,y,slp):
    im = pyautogui.screenshot()
    img = im.getpixel((x,y))
    print (img)
    if (img[0] == 99):
        main()
    else:
        pyautogui.moveTo(x,y, duration=0.25)
        pyautogui.click(x,y)
        print('Clicked ' + str(x) + ', ' + str(y) + '.')
        slp = slp * 10
        time.sleep(slp)
        print('Slept ' + str(slp) + '.')

def main():
    i = 0
    while(1):
        x = random.randint(1500,1600)
        y = random.randint(1000,1100)
        slp = random.random()
        go(x,y,slp)
        i=i+1

main()