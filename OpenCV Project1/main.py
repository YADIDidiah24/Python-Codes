import cv2
import handtracking as HT  # Make sure to replace this with the correct import if needed
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import numpy as np
import pyautogui
import functions

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = interface.QueryInterface(IAudioEndpointVolume)
volRange = volume.GetVolumeRange()

minVol = volRange[0]
maxVol = volRange[1]
pyautogui.FAILSAFE = False

wCam, hCam = 1024, 576
frameR = 100
cap = cv2.VideoCapture(0)  # 1 for phone camera
cap.set(3, wCam)
cap.set(4, hCam)
detector = HT.HandDetector()
imgCanvas = np.zeros((hCam, wCam, 3), np.uint8)

vol = 0
volBar = 300
volPercent = 0
volume_control_enabled = False
draw_mode_enabled = False
mouse_enabled = False
wScr, hScr = pyautogui.size()
xp, yp = 0, 0

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img)

    if volume_control_enabled:
        if lmList:
            functions.volumeControl(img, lmList[0][1], lmList[4][1], lmList[8][1], lmList[12][1], lmList[16][1])

    if draw_mode_enabled:
        if lmList:
            fingers = detector.fingersUp()
            imgCanvas, img = functions.draw(img, fingers, lmList[8][1], lmList[8][2])

    if mouse_enabled:
        if lmList:
            fingers = detector.fingersUp()
            functions.mouse(img, fingers, lmList[8][1], lmList[12][1], lmList[16][1], (lmList[12][1] + lmList[16][1]) // 2,
                  (lmList[12][2] + lmList[16][2]) // 2)

    functions.checkKeyPresses(img, lmList)

    cv2.imshow("Hand Tracking", img)
    cv2.waitKey(1)
