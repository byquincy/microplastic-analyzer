import cv2
import numpy as np
import matplotlib.pyplot as plt

import formobile

cap = cv2.VideoCapture(0)
cap = formobile.wait(cap)

qcd = cv2.QRCodeDetector()
plt.ion()
fig, ax = plt.subplots()
ax.set_ylim(0, 255)

if not cap.isOpened():
    print("Error: could not open video device.")
    exit(-1)

while True:
    ret, frame = cap.read()
    # axis=0: 가로   |   axis=1: 세로

    decoded_info = qcd.detectAndDecode(frame)[0]
    if decoded_info != None:
        print(decoded_info)
    
    cv2.imshow("Cam Test", frame)
    if cv2.waitKey(1) == 27:
        break
    
    # y = np.max(frame, axis=0)

    # ax.clear()
    # ax.plot(range(len(y)), y)
    
    # plt.show()

cap.release()
cv2.destroyAllWindows()