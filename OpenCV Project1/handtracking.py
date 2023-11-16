import cv2
import mediapipe as mp
import time


class HandDetector():

    def __init__(self, mode=False, maxHands=2, modelComplexity=1,detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon
        self.modelComplex = modelComplexity
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands,self.modelComplex, self.detectionCon, self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils
        self.tipIds = [4, 8, 12, 16, 20]

    def findHands(self,img,draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)


        if self.results.multi_hand_landmarks:
            for handlmrk in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handlmrk, self.mpHands.HAND_CONNECTIONS,
                                        self.mpDraw.DrawingSpec(color=(252, 3, 3)),
                                        self.mpDraw.DrawingSpec(color=(15, 255, 80)))
        return img
    def findPosition(self, img, handNo=0,draw=True):
        self.lmList =[]
        if self.results.multi_hand_landmarks:
            Myhand = self.results.multi_hand_landmarks[handNo]
            for id,lm in enumerate(Myhand.landmark):
                h, w, c = img.shape
                cx,cy = int(lm.x*w), int(lm.y*h)
                self.lmList.append([id,cx,cy])
        return self.lmList
            
    def fingersUp(self):
        fingers= []

        if len(self.lmList) >= max(self.tipIds):
            for finger in self.tipIds:
                if self.lmList[finger][1] < self.lmList[finger - 1][1]:
                    fingers.append(1)
                else:
                    fingers.append(0)

        return fingers


