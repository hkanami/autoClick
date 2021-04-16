
import pyautogui as gui
#from PIL import pil
import cv2
import numpy as np
import logging.config
import time
import sys
import io
import json

def getScreen():
    pil_sc=gui.screenshot()

    cv_image = np.array(pil_sc) 

    cv_image = cv_image[:, :, ::-1].copy()
    cm=cv2.imread('target.png')
    m_map = cv2.matchTemplate(cv_image, cm, cv2.TM_CCOEFF_NORMED)
    return m_map
    
def click_bottom():

    t1=time.time()
    delay=2
    while True:
        time.sleep(0.01)
        t2=time.time()
        if (t2-t1)<delay:
            continue
        m_map=getScreen()
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(m_map) 
        if max_val >0.7: 
            gui.click(max_loc)
            print(max_loc )
        t1=time.time()

def main():
    click_bottom()

if __name__ == '__main__':

    try:
        main()
    except SystemExit:
        pass