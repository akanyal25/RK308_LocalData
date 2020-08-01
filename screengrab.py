import numpy as np
import cv2

from PIL import ImageGrab




while True:
    img = ImageGrab.grab()
    img_np = np.array(img)

    frame = cv2.cvtColor(img_np,cv2.COLOR_BGR2RGB)

    cv2.imshow("Screen" , frame)


    if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cv2.destroyAllWindows()