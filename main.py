import cv2
import numpy as np

num_down =2
num_bilateral =7

# img_rgb = cv2.imread("avatar.png")
cap = cv2.VideoCapture(0)


while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    img_rgb= cv2.resize(frame, (900,900))

    img_color = img_rgb

    for _ in range(num_down):
        img_color = cv2.pyrDown(img_color)

    for _ in range(num_bilateral):
        img_color = cv2.bilateralFilter(img_color, d=9, sigmaColor=9,sigmaSpace=7)

    for _ in range(num_down):
        img_color = cv2.pyrUp(img_color)

    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    img_blur = cv2.medianBlur(img_gray, 7)

    img_edge = cv2.adaptiveThreshold(img_blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, blockSize=9, C=2)

    img_edge = cv2.cvtColor(img_edge, cv2.COLOR_GRAY2RGB)
    img_cartoon = cv2.bitwise_and(img_color, img_edge)

    stack = np.hstack([img_rgb, img_cartoon])
    cv2.imshow('Stacked Images', stack)
    # Display the resulting frame
    # cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
