import pyautogui
import os

import time
import pygetwindow as pw


def generate_ppt(text):
    url = 'https://app.simplified.com/design/generate-ai/presentation'
    
    edge_path = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
    
    os.system(f'"{edge_path}" --app={url}')
    pyautogui.press('enter')
    time.sleep(15)
    windows = pw.getWindowsWithTitle("Simplified")
    if windows:
        window = windows[0]
        window.activate()
        time.sleep(10)
        #pyautogui.click(x=190, y=202)
        pyautogui.moveTo(x=190, y=203, duration=1)  
        time.sleep(5)  
        pyautogui.click()
        pyautogui.write(text,interval=0.1)
        time.sleep(3)
        pyautogui.moveTo(x=1113, y=505, duration=1)  
        time.sleep(3)
        pyautogui.click()
        pyautogui.moveTo(x=1068, y=925, duration=1)
        time.sleep(3)
        pyautogui.click()

#generate_ppt("generate ppt on ai")

    
    