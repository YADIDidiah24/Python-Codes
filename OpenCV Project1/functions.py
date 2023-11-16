import cv2
import time
import handtracking as HT
import math
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import numpy as np
import pyautogui

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = interface.QueryInterface(IAudioEndpointVolume)
volRange = volume.GetVolumeRange()

minVol = volRange[0]
maxVol = volRange[1]
pyautogui.FAILSAFE = False

wCam, hCam= 1024,576
frameR = 100
cap = cv2.VideoCapture(0) # 1 for phone camera
cap.set(3,wCam)
cap.set(4,hCam)
detector = HT.HandDetector()
imgCanvas = np.zeros((hCam, wCam, 3), np.uint8) 

vol=0
volBar=300
volPercent=0
volume_control_enabled = False 
draw_mode_enabled = False
mouse_enabled = False
wScr, hScr = pyautogui.size()
xp,yp=0,0
# Function to control volume based on hand position
def volumeControl(img,lmList,x1,y1,x2,y2): 
    cx,cy = (x1+x2)//2 ,(y1+y2)//2
    cv2.circle(img,(x1,y1),10,(255, 165, 0),cv2.FILLED)
    cv2.circle(img,(x2,y2),10,(255, 165, 0),cv2.FILLED)
    cv2.line(img,(x1,y1),(x2,y2),(255, 165, 0),3,cv2.FILLED)
    cv2.circle(img,(cx,cy),10,(255, 255, 255),cv2.FILLED)

    length = math.hypot(x2-x1,y2-y1)
    # hand range = 15 - 150
    # vol range = -65 - 0

    vol = np.interp(length,[15,120],[minVol,maxVol])
    volBar = np.interp(length,[15,120],[400,150])
    volPercent = np.interp(length,[15,120],[0,100])
    volume.SetMasterVolumeLevel(vol, None)

    if length<20:
        cv2.circle(img,(cx,cy),10,(0, 0, 0),cv2.FILLED)
    cv2.rectangle(img,(50,150),(85,400),(0,255,0),3)
    cv2.rectangle(img,(50,int(volBar)),(85,400),(0,255,0),cv2.FILLED)    
    cv2.putText(img, f"Volume = {int(volPercent)} %", (40, 450), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,255,0),1)
# Function to draw on the canvas

def draw(img, fingers, x1, y1):
    global xp, yp, imgCanvas
    if len(fingers) != 0 and not fingers[1]:
        return imgCanvas, img
    if len(fingers) != 0 and fingers[1]:
        if xp == 0 and yp == 0:
            xp, yp = x1, y1

        cv2.line(imgCanvas, (xp, yp), (x1, y1), (8, 8, 196), 10)
        xp, yp = x1, y1
       
        imgGray = cv2.cvtColor(imgCanvas, cv2.COLOR_BGR2GRAY)
        _, imgInv = cv2.threshold(imgGray, 50, 255, cv2.THRESH_BINARY_INV)
        imgInv = cv2.cvtColor(imgInv, cv2.COLOR_GRAY2BGR)

       
        img = cv2.bitwise_and(img, imgInv)
        img = cv2.bitwise_or(img, imgCanvas)

    return imgCanvas,img
# Function to control the mouse

def mouse(img,finger,x1,y1,x2,y2,x_middle,y_middle):
    x3 = np.interp(x1,(frameR,wCam-frameR),(0,wScr))
    y3 = np.interp(y1,(frameR,hCam-frameR),(0,hScr))

    if finger[1]==1 :
        pyautogui.moveTo(wScr-x3,y3)
        x1 = x1*wScr
        y1 = y1*hScr
        x3 = x3*wScr
        y3 = y3*hScr
        cv2.rectangle(img,(frameR,frameR),(wCam-frameR,hCam-frameR),(215,5,247),2)
        cv2.circle(img,(x1,y1),15,(3,98,252),cv2.FILLED)
    if finger[0]==1 :
        x1 = x1*wScr
        y1 = y1*hScr
        x3 = x3*wScr
        y3 = y3*hScr
        cv2.circle(img,(x1,y1),15,(3,98,252),cv2.FILLED)

    distance_between_2 = math.dist((x1, y1), (x2, y2))

    distance_1 = math.dist((x1, y1), (x2, y2))
    distance_2 = math.dist((x1, y1), (x_middle, y_middle))
    distance_3 = math.dist((x2, y2), (x_middle, y_middle))
    threshold_distance =20
    if distance_1 < threshold_distance and distance_2 < threshold_distance and distance_3 < threshold_distance:
        pyautogui.rightClick()
    if distance_between_2 < threshold_distance:
        pyautogui.click()
# Function to handle key presses

def checkKeyPresses(img,lmList):
    global volume_control_enabled
    global draw_mode_enabled
    global mouse_enabled
    key = cv2.waitKey(1) & 0xFF
    if key == ord('1'):  
        exit(0)
    if key == ord('q'):
        volume_control_enabled = False
        draw_mode_enabled = False
        mouse_enabled = False
    if key == ord('v'):
        volume_control_enabled = True
    if key ==ord("d"):
        draw_mode_enabled = True
    if key == ord("c"):
        global imgCanvas 
        imgCanvas = np.zeros((hCam,wCam,3),np.uint8)
    if key == ord("m"):
        mouse_enabled = True
        