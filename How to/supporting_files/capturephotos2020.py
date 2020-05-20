# This code captures photos from a webcam by finding faces and storing them as 256x256 pngs
# Prior to taking photos, empty folder named as photodir (search below)
# Photo set up:
#   Ensure white background with no other facial images (webcam will otherwise capture images from posters)
#
# Overview of image capture procedure
#   Once webcam image is in view, put cursor in the webcam window and
#   Press SPACE to take the photo:
#   Press q to quit
# The default is to save the photos with in a subfolder relative to the capture code, name stored in photodir
#
# To run: You need python (version 3.x)
#     Open a command window and navigate to this folder
#     1. Type python capturephotos2020.py firstname_lastinitial_smile
#     2. Make sure the name has no spaces
#     3. Put cursor in image window; Capture 4 images of smiling
#     4. With cursor in window, press "q"
#     5. Use UP arrow at the command line, delete "smile" from firstname_lastinitial_smile
#     6. Repeat steps 3 & 4 to capture 4 non-smiling photos
#
#     For live demo, type livedemo instead of student_name, this will write to Sandbox, if it is mapped as X:


import numpy as np
import cv2
import sys

if len(sys.argv) < 2:
    print("USAGE: ./capture.py student_name(no spaces please)")
    print("For livedemo, type livedemo instead of student name")
    sys.exit(-1)

student_name = sys.argv[1]
cap = cv2.VideoCapture(1)
photodir = "./ProjectImages/"
print("Photos stored in ",photodir, ", update photodir variable in code to change")
print("Press SPACE to take photo, press q to quit")

counter = 0
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    faces = face_cascade.detectMultiScale(frame, scaleFactor=1.2, minSize=(20,20))
    frame_copy = np.copy(frame)
    # flip horizontally for display (so it is like a mirror)
    frame_copy = cv2.flip(frame_copy, 1)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame_copy,(frame.shape[1]-x,y),(frame.shape[1] - (x+w),y+h),(0,0,255))

    # compute lower and upper bounds of the window
    x_lower = int(frame.shape[1]*0.4)
    y_lower = int(frame.shape[0]*0.25)
    x_upper = int(frame.shape[1]*0.6)
    y_upper = int(frame.shape[0]*0.75)

    #cv2.rectangle(frame_copy, (x_lower, y_lower),
    #                         (x_upper, y_upper),
    #                         (0,0,255))
    cv2.imshow('frame',frame_copy)
    key = cv2.waitKey(5)
    #print key
    if key & 0xFF == ord(' '):
        for (x,y,w,h) in faces:
            pixels = frame[y:y+min(h,w), x:x+min(h,w)]

            resized_image = cv2.resize(pixels, (256, 256))
            if student_name == "livedemo":
                cv2.imwrite("X:/QEA/Faces/faceimagetest.png" , resized_image)
                print("Photo taken: X:/QEA/Faces/faceimagetest.png")
            else:
                cv2.imwrite("%sfaceimage_%s_%02d.png" %(photodir,student_name, counter), resized_image)
                print("Photo taken:",photodir,"faceimage_",student_name,"_", counter,".png")
            counter += 1

    elif key & 0XFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
