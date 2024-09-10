import cv2
from cvzone.HandTrackingModule import HandDetector
import time


    
class Button:
    def __init__(self, pos, width, height, value):
        self.pos = pos
        self.width = width
        self.height = height
        self.value = value

    def draw(self, img):
        cv2.rectangle(img, self.pos, (self.pos[0] + self.width, self.pos[1] + self.height), (225, 225, 225), cv2.FILLED)
        cv2.rectangle(img, self.pos, (self.pos[0] + self.width, self.pos[1] + self.height), (50, 50, 50), 3)
        cv2.putText(img, self.value, (self.pos[0] + 40, self.pos[1] + 60), cv2.FONT_HERSHEY_PLAIN, 2, (50, 50, 50), 2)
    
    def checkClick(self, X, Y):
        if self.pos[0] < X < self.pos[0] + self.width and \
           self.pos[1] < Y < self.pos[1] + self.height:
            cv2.rectangle(img, self.pos, (self.pos[0] + self.width, self.pos[1] + self.height), (225, 225, 225), cv2.FILLED)
            cv2.rectangle(img, self.pos, (self.pos[0] + self.width, self.pos[1] + self.height), (50, 50, 50), 3)
            cv2.putText(img, self.value, (self.pos[0] + 25, self.pos[1] + 80), cv2.FONT_HERSHEY_PLAIN, 5, (0, 0, 0), 5)
            return True
        else:
            return False

# Webcam
cap = cv2.VideoCapture(0)  # Use camera index 0 for the default camera
cap.set(3, 1280)  # width
cap.set(4, 720)  # height
detector = HandDetector(detectionCon=0.8, maxHands=1)

# Creating Buttons
ButtonListValues = [['7', '8', '9', '*'],
                    ['4', '5', '6', '-'],
                    ['1', '2', '3', '+'],
                    ['0', '/', '.', '=']]
ButtonList = []
for X in range(4):
    for Y in range(4):
        xpos = X * 100 + 800
        ypos = Y * 100 + 150
        ButtonList.append(Button((xpos, ypos), 100, 100, ButtonListValues[Y][X]))

# Variables
myEquation = ''
delayCounter = 0

# Loop
while True:
    # Get image from webcam
    success, img = cap.read()
    img = cv2.flip(img, 1)

    # Detection of hand
    hands, img = detector.findHands(img, flipType=False)

    # Draw all buttons
    cv2.rectangle(img, (800, 50), (800 + 400, 70 + 100), (225, 225, 225), cv2.FILLED)
    cv2.rectangle(img, (800, 50), (800 + 400, 70 + 100), (50, 50, 50), 3)
    for button in ButtonList:
        button.draw(img)

    # Check for Hand
    if hands:
        lmList = hands[0]['lmList']
        x1, y1 = lmList[8][0:2]
        x2, y2 = lmList[12][0:2]
        length, _, img = detector.findDistance((x1, y1), (x2, y2), img)
        X, Y = x1, y1
        if length < 50:
            for i, button in enumerate(ButtonList):
                if button.checkClick(X, Y) and delayCounter ==0:
                    myValue = ButtonListValues[int(i % 4)][int(i / 4)]
                    if myValue == "=":
                       myEquation = str(eval(myEquation))
                    else:   
                        myEquation += myValue
                    delayCounter = 1     
                        
    # Avoid Duplicates
    if delayCounter != 0:
        delayCounter +=1
        if delayCounter >10:
            delayCounter =0                    

    # Display the Equation/Result
    cv2.putText(img, myEquation, (810, 120), cv2.FONT_HERSHEY_PLAIN, 3, (50, 50, 50), 3)

    # Display Image
    cv2.imshow("Image", img)
    key = cv2.waitKey(1)
    if key == ord('c'):
        myEquation = ''
    
    # Check for key press to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to quit
        break

# Release the camera and close OpenCV windows
cap.release()
cv2.destroyAllWindows()
