import time
import random
import pyautogui
print (pyautogui.size())

time.sleep(5)
pyautogui.click()    # click to put drawing program in focus
distance = 200
while distance > 0:
      pyautogui.dragRel(distance, 0, duration=0)  
      distance = distance - 5
      pyautogui.dragRel(0, distance, duration=0)  
      pyautogui.dragRel(-distance, 0, duration=0) 
      distance = distance - 5
      pyautogui.dragRel(0, -distance, duration=0) 
