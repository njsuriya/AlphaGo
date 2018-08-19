
# import the necessary packages
from imutils.video import VideoStream
from imutils import face_utils

import pygame,dlib,time,cv2,os
pygame.init()

shape_predictor="shape_predictor_68_face_landmarks.dat" 
# initialize dlib's face detector (HOG-based) and then create
# the facial landmark predictor
print("[loading facial landmark predictor...")
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(shape_predictor)

# initialize the video stream and allow the cammera sensor to warmup
print("camera sensor warming up...")
vs = VideoStream(src=0).start()

time.sleep(2.0)

j=0
p=[(0,0)]*68
p1=[(0,0)]*68
d=[(0,0)]*68
dist_smilo=0
dist_leyeo=0
dist_reyeo=0
dist_ango=0
dup1,dup2=0,0
diff_chx,diff_chy=0,0
pid=0
count_smile,count_eact,count_be=0,0,0
# loop over the frames from the video stream
while True:
        
        frame = vs.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # detect faces in the grayscale frame
        rects = detector(gray)
        diff_smile=0
        diff_ang=0
        diff_leye=0
        diff_eye=0
        diff_reye=0
        diff_up=0
        diff_change=0
        if True:
                p=p1
                p1=[(0,0)]*68
                d=[(0,0)]*68
        cv2.imshow("Frame", frame)
        # loop over the face detections
        x49=0
        y49=0
        x55=0
        y55=0
        x23=0
        y23=0
        x22=0
        y22=0
        x38=0
        y38=0
        x41=0
        y41=0
        x44=0
        y44=0
        x47=0
        y47=0
        print('count_eact,count_smile,count_be',count_eact,count_smile,count_be)

        e,s,le,re,be=0,0,0,0,0
        for rect in rects:
                # determine the facial landmarks for the face region, then
                # convert the facial landmark (x, y)-coordinates to a NumPy Array
                
                

                shape = predictor(gray, rect)
                shape = face_utils.shape_to_np(shape)

                # loop over the (x, y)-coordinates for the facial landmarks
                # and draw them on the image
                i=1
                print('iter'+str(j))
                x1,y1,w,h=0,0,0,0
                j=j+1
                for (x, y) in shape:
                        #print(i)
                        cv2.circle(frame, (x, y), 1, (0, 0, 255), -1)

                        #print(x,y)
                        if(i):
                                cv2.putText(frame, str(i), (x, y),cv2.FONT_HERSHEY_SIMPLEX, 0.3, (0, 0, 255), 1)
                        #if j==1:
                        if i==1:
                                x1=x
                                y1=y
                                
                                
                                if j%2!=0:
                                        dup1=x1
                                        dup2=y1
                                        print('dup',dup1,dup2)
                                        diff_chx,diff_chy=0,0
                                else:
                                        diff_chx=dup1-x1
                                        print(dup1)
                                        
                                        print('change',diff_chx)
                                        diff_chy=dup2-y1
                                        print(dup2)
                                        
                                        print('change',diff_chy)
                                

                        elif i==9:
                                h=y-y1
                        elif i==17:
                                w=x-x1

                        if i==20:
                                if j%2!=0:
                                        y_20=y-y1
                                        print(y_20)
                                else:
                                        y20=y-y1
                                        diff_up=y_20-y20
                                        print(y20,diff_up)
                                        
                                
                        
                        elif(i==49):
                                x49=x
                                y49=y
                        elif(i==55):
                                x55=x
                                y55=y

                                dist_smile=((x49-x55)**2+(y49-y55)**2)**0.5  #distance formula
                                print('dist-smile',dist_smile)
                                diff_smile=(dist_smile)-dist_smilo
                                if diff_smile<0:
                                        diff_smile*=-1

                                print('diff-smile',diff_smile)
                                
                                print('dist-smilo',dist_smilo)
                                if j==1 or diff_smile>15:
                                        dist_smilo=dist_smile
                                        
                                        
                                if diff_smile<6:
                                        dist_smilo=(dist_smilo+dist_smile)//2

                        elif(i==38):
                                x38=x
                                y38=y
                        elif(i==41):
                                x41=x
                                y41=y
                                dist_leye=((x38-x41)**2+(y38-y41)**2)**0.5
                                print('dist-lefteye',dist_leye)
                                diff_leye=(dist_leye)-dist_leyeo

                                if diff_leye<0:
                                        diff_leye=diff_leye*-1

                                print('diff-leye',diff_leye)
                                
                                print('dist-leyeo',dist_leyeo)
                                if j==1 or diff_leye>2:
                                        dist_leyeo=dist_leye
                                        
                                        
                                if diff_leye<1:
                                        dist_leyeo=(dist_leyeo+dist_leye)//2                                
                        elif(i==44):
                                x44=x
                                y44=y
                        elif(i==47):
                                x47=x
                                y47=y
                                dist_reye=((x44-x47)**2+(y44-y47)**2)**0.5
                                print('dist-reye',dist_reye)
                                diff_reye=(dist_reye)-dist_reyeo

                                if diff_reye<0:
                                        diff_reye=diff_reye*-1

                                print('diff-reye',diff_reye)
                                
                                print('dist-reyeo',dist_reyeo)
                                if j==1 or diff_reye>2:
                                        dist_reyeo=dist_reye
                                print('check both')
                                print(diff_leye,diff_reye)
                                diff=(dist_reye-dist_leye)-(dist_reyeo-dist_leyeo)
                                if diff<0:
                                        diff=diff*-1
                                if diff_leye+diff_reye>2 and diff_leye+diff_reye<4 and (diff<0.5):
                                        print('check both')
                                        diff_eye=1
                                        
                                '''if diff_leye>2.5 and diff_reye>2.5 and j!=1:
                                        print('check both')
                                        print(diff_leye,diff_reye)'''
                                        
                                if diff_reye<1:
                                        dist_reyeo=(dist_reyeo+dist_reye)//2   
        
                        
                        
                        
                       
                        
                        #cv2.rectangle(frame,(x1,y1),(x1+w,y1+h),(255,0,0),2)5
                        if diff_chx<10 and diff_chy<10:
                                
                                if diff_smile>10 and diff_smile<50 and j!=1:
                                        cv2.putText(frame,'Smile', (50, 50),cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 1)
                                        s=1
                                        cv2.imshow("Snapshot_Smile_Selfie", frame)

                                elif diff_up>3:
                                        cv2.putText(frame,'Eye act', (50, 50),cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 1)
                                        e=1

                                elif diff_eye==1: 
                                        
                                        print('Both eye')
                                        be=1

                                        
                                elif diff_leye>2.5 and diff_leye<5:
                                        
                                        pid=os.getpid()
                                        print(pid)
                                        
                                        
                                        cv2.putText(frame,'Right eye', (50, 50),cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 1)
                                        le=1
                                        
                                        

                                elif diff_reye>2.5 and diff_reye<5:
                                        pygame.mixer.music.stop()
                                        cv2.putText(frame,'Leye', (50, 50),cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 1)
                                        re=1


                        i=i+1

        if e:
                pygame.mixer.music.load('song.mp3')
                pygame.mixer.music.play(-1)                
                print('eye act')
                count_eact=count_eact+1
        elif s:
                print('smile')
                count_smile=count_smile+1
        # show the frame
        elif be:
                print('Bothe')
                count_be=count_be+1
        elif le:
                h=1
                

        cv2.imshow("Frame", frame)
       
        key = cv2.waitKey(1) & 0xFF
        #if j==15:
        #        break
        # if the `q` key was pressed, break from the loop
        if key == ord("q"):
                break
 
# do a bit of cleanup
VideoStream(src=0).stop()
cv2.destroyAllWindows()


