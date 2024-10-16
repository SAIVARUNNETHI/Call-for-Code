

import pyautogui
import time
import os
import pygetwindow as gw

def generate_image(text):
    url = 'https://www.craiyon.com/'
    edge_path = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
    os.system(f'"{edge_path}" --app={url}')
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.moveTo(x=389,y=620,duration=1)
    pyautogui.click()
    time.sleep(3)
    pyautogui.write(text,interval=0.1)
    pyautogui.press('enter')
    

#generate_image("generate an image of dog riding a bicycle")
