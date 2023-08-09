import time 
import random
import pyautogui

def ran(l,b):
    return random.randint(l,b)/10

def left93(layers):
    for layer in range(layers):
        letter = 'd'
        if (layer % 2) == 0:
            letter = 'a'
        pyautogui.keyDown('shift')
        pyautogui.keyDown(letter)
        time.sleep(125)
        time.sleep(ran(2,10))
        pyautogui.keyUp(letter)
        pyautogui.keyUp('shift')
        time.sleep(ran(2,10))
    pyautogui.keyUp('shift')
    pyautogui.press('/')
    time.sleep(1)
    pyautogui.typewrite('warp garden')
    pyautogui.press('enter')
    

def right93(layers):
    for layer in range(layers):
        letter = 'a'
        if (layer % 2) == 0:
            letter = 'd'
        pyautogui.keyDown('shift')
        pyautogui.keyDown(letter)
        time.sleep(119)
        time.sleep(ran(2,10))
        pyautogui.keyUp(letter)
        time.sleep(ran(2,10))
    pyautogui.keyUp('shift')    
    pyautogui.press('up')
    
    
def Pumpkin():
    for row in range(9):
        letter = 'a'
        if (row % 2) == 0:
            letter = 'd'
        pyautogui.keyDown('shift')
        pyautogui.keyDown(letter)
        time.sleep(102)
        time.sleep(ran(2,10))
        pyautogui.keyUp('shift')
        pyautogui.keyUp(letter)
        pyautogui.keyDown('w')
        time.sleep(ran(20,25))
        pyautogui.keyUp('w')
        

def countDown(s):
    for second in range(s,0,-1):
        print(second)
        time.sleep(1)
        
countDown(5)
left93(5)
time.sleep(2)
left93(5)
time.sleep(2)
left93(5)
time.sleep(2)
left93(5)
time.sleep(2)
left93(5)

#if choice == 1:
    #left93(5)
    #time.sleep(5)
    #left93(5)
    #time.sleep(5)
    #left93(5)
#else:
    #right93(5)
    
        
