import matplotlib
matplotlib.use('TkAgg')

import numpy as np
import cv2
import matplotlib.pyplot as plt

import analyzeFunction
import formobile

fig = plt.figure()
cap = cv2.VideoCapture(1)
cap = formobile.wait(cap)

testFunction = analyzeFunction.getMax

# initialize
ret,frame = cap.read()
x, y = testFunction(frame)


line1, = plt.plot(x, y)        # so that we can update data later
plt.ylim((0, 256))

while True:
    ret,frame = cap.read()

    # update data
    line1.set_ydata(testFunction(frame)[1])

    # redraw the canvas
    fig.canvas.draw()

    # convert canvas to image
    figImg = np.asarray(fig.canvas.buffer_rgba())

    # img is rgba, convert to opencv's default bgr
    figImg = cv2.cvtColor(figImg,cv2.COLOR_RGBA2BGR)


    cv2.imshow("plot",figImg)
    cv2.imshow("cam",frame)

    k = cv2.waitKey(33) & 0xFF
    if k == 27:
        break