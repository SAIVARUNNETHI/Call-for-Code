import pyautogui
import time
import pygetwindow as gw
import os
 

def interact_with_ai_service(question):
    
    
    url = 'https://gemini.google.com/'
   
    edge_path = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
    
    os.system(f'"{edge_path}" --app={url}')
    pyautogui.press('enter')
    time.sleep(5) 
    #pyautogui.hotkey('alt', 'tab')
    windows = gw.getWindowsWithTitle("Gemini")
    if windows:
        window = windows[0]
        window.activate()
        time.sleep(1)
        pyautogui.write(question, interval=0.1)
        pyautogui.press('enter')







