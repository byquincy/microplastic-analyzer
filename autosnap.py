import cv2
import numpy as np

import hashlib
import base64

import formobile

START_COORD = (10, 10)
END_COORD = (400, 400)

cap = cv2.VideoCapture(1)
cap = formobile.wait(cap)

qcd = cv2.QRCodeDetector()
enc = hashlib.md5()

if not cap.isOpened():
    print("Error: could not open video device.")
    exit(-1)

lastInfo = None
lastFrame = None
while True:
    ret, frame = cap.read()
    # axis=0: 가로   |   axis=1: 세로

    decodedInfo = qcd.detectAndDecode(frame)[0]
    if decodedInfo != "":
        if lastInfo == decodedInfo:
            lastFrame = frame.copy()
        else:
            if lastInfo != None:
                print("Save: %s"%lastInfo)
                enc.update(lastInfo.encode())
                np.save("./image4analyze/%s"%base64.urlsafe_b64encode(enc.digest()).decode(), lastFrame)

            print(decodedInfo)
            lastInfo = decodedInfo
            lastFrame = frame.copy()
    
    cv2.imshow("Cam Test", frame)
    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()