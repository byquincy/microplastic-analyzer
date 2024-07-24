import json
import numpy as np
import cv2

import hashlib
import base64

with open("QR_LIST.json", encoding="utf-8") as f:
    qrDict:dict = json.load(f)
enc = hashlib.md5()

for info, explanation in qrDict.items():
    enc.update(info.encode())
    fileName = base64.urlsafe_b64encode(enc.digest()).decode()

    img = np.load("./image4analyze/%s.npy"%fileName)

    cv2.imshow("%s: %s"%(info, explanation), img)
    cv2.waitKey(0)

cv2.destroyAllWindows()