import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    lower_red = np.array([0, 100, 100])
    upper_red = np.array([10, 255, 255])
    red_mask=cv2.inRange(hsv,lower_red,upper_red)

    lower_red = np.array([170, 100, 100])
    upper_red = np.array([180, 255, 255])
    red_mask1=cv2.inRange(hsv,lower_red,upper_red)

    real_red_mask = red_mask+red_mask1

    result = cv2.bitwise_and(frame, frame, mask=real_red_mask)


    cv2.imshow("Original video camera", frame)
    cv2.imshow("Red object dedector camera", frame)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
