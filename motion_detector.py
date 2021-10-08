import cv2, time
from datetime import date, datetime

first_frame=None
status_list=[None,None]
times=[]
captureDevice = cv2.VideoCapture(0, cv2.CAP_DSHOW) #captureDevice = camera


# Iterating of the first frame
while True:
    #Capture the first frame
    check, frame = captureDevice.read()
    status=0
    #converts to gray, and gaussian
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray=cv2.GaussianBlur(gray,(21,21),0)

    # store first frame value
    if first_frame is None: 
        first_frame=gray
        continue
    
    #calculate difference find countour
    delta_frame=cv2.absdiff(first_frame,gray)
    tresh_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    
    tresh_frame=cv2.dilate(tresh_frame, None, iterations=2)

    #Distinct area get contours, will be stored in cnts
    (cnts,_) =cv2.findContours(tresh_frame.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    #Keep countours area bigger than 1000px
    #Goto: next contours
    for countour in cnts:
        if cv2.contourArea(countour) < 1000:
            continue 
        status=1
        (x, y, w, h)=cv2.boundingRect(countour)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 3)
    status_list.append(status)
    if status_list[-1]==1 and status_list[-2]==0:
        times.append(datetime.now())
    if status_list[-1]==0 and status_list[-2]==1:
        times.append(datetime.now())

    cv2.imshow("Gray Frame",gray)
    cv2.imshow("Delta Frame",delta_frame)
    cv2.imshow("Treshold",tresh_frame)
    cv2.imshow("Color Frame", frame)


    key = cv2.waitKey(1)
   
    if key==ord('q'):
        if status==1:
            times.append(datetime.now())
        break
print(status_list)
print(times)
captureDevice.release()
cv2.destroyAllWindows