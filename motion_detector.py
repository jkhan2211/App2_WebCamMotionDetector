import cv2, time

first_frame=None
captureDevice = cv2.VideoCapture(0, cv2.CAP_DSHOW) #captureDevice = camera



while True:
    a = a +1 
    check, frame = captureDevice.read()

    if first_frame is None: 
        first_frame=gray

    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("Capturing",gray)

    key = cv2.waitKey(1)

    if key==ord('q'):
        break
captureDevice.release()
cv2.destroyAllWindows