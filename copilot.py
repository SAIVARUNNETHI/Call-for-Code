import pyautogui
import time

time.sleep(2)

def task(question):
    pyautogui.hotkey('win','c')

    time.sleep(2)
    pyautogui.write(question,interval=0.1)

    pyautogui.press('enter')