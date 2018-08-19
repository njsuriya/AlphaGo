# AlphaGo
Dlibs Facial Landmark Detector:
 
The pre-trained facial landmark detector inside the dlib library is used to estimate the location of 68 (x, y)-coordinates that map to 
facial structures on the face
The above figure shows the visualizing the 68 facial landmark coordinates (iBUG 300-W dataset)	
The facial landmark detector included in the dlib library is an implementation of the One Millisecond Face Alignment with an Ensemble of 
Regression Trees paper by Kazemi and Sullivan (2014) in IEEE.

Imutlis:

A series of convenience functions to make basic image processing functions such as translation, rotation, resizing, skeletonization, and 
displaying matplotlib images easier with OpenCV

Functions Performed in this...
           
By detecting the facial Co-ordinate movement for a specific facial expression doing a specific task.
The python code detects different landmarks on the face and predicts the emotions such as smile based on it. It automatically takes a 
snapshot of that person when he smiles. Also when the two eyebrows are lifted up, the system plays a music automatically and the music 
stops when you blink your right eye.
Detecting Different facial expressions:
From the pre-trained facial landmark.jpg included in this,
To detect smile in a face, points 49 and 50 are considered. The distance between those points increases when a person smiles and that is 
used here to detect a smile.
To detect left eye brow movement (lifting up), points 38 and 41 are considered. The distance between those points increases when a 
person smiles and that is used here to detect a smile.
Similarly to detect right eye brow movement (lifting up), points 44 and 47 are considered. The distance between those points increases 
when a person smiles and that is used here to detect a smile.



Yet to include....
By detecting the eyes co-ordinate points, finding the drowsiness(state of feeling sleepy) while driving. If the drowsiness condition 
activates the car automatically makes an alarm.
Also playing the mp3 player in car/house using our facial gesture instead of playing with remotes.
In E-Reader with our eye reactions, we can scroll down/up the pages.

Performing as much as possible functions with facial gestures in suitable places
