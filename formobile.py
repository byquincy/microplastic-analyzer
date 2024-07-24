import cv2
import time

WAIT_TIME = 1

def wait(cap):
    start = time.time()
    while time.time() - start < WAIT_TIME:
        print("\r%.2f"%(WAIT_TIME - (time.time() - start)), end="")

        try:
            ret, frame = cap.read()
        except Exception as e:
            start = time.time()
            print(e)
            cap = cv2.VideoCapture(1)
            continue
    print("\r시작합니다.")
    
    return cap