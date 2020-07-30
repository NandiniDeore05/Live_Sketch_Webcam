# Live Sketch Using Webcam

import cv2
import numpy as np

# Sketch Genrating Function
def sketch(image):
    # Converting the image to Grayscale
    gray = cv2.cvtColor(image , cv2.COLOR_BGR2GRAY )
    
    # Clean up image using Gaussian Blur
    gray_blur = cv2.GaussianBlur(gray, ksize=(5,5), sigmaX=0)
    
    #Extracting The Edges
    Canny_edge = cv2.Canny(gray_blur, threshold1=10, threshold2=70)
    
    # Doing an invert binarize the image
    # Since Canny o/p will bewith black background hence inversion is used to get a feel of sketch
    # We can also use biwise OR for inversion
    _ , mask = cv2.threshold(Canny_edge, thresh=70, maxval=255, type=cv2.THRESH_BINARY_INV)
    return mask

# Initializing the webcam 
cam = cv2.VideoCapture(0)  # 0 is for webcam & 1 for external source

while True:
    _ , frame = cam.read()
    cv2.imshow('Live Sketcher' , sketch(frame))
    if cv2.waitKey(1) == 13:      # Press " ENTER KEY TO CLOSE WINDOW "
        break
    
# Releasing The Cam & Closing all windows
cam.release()
cv2.destroyAllWindows()