# import required libraries
import cv2
import numpy as np
  
# define a video capture object
vid = cv2.VideoCapture(0)
  
while(True):  
    # Capture the video frame
    # by frame
    ret, frame = vid.read()
    if(ret == False):
        break
    # Display the resulting frame
    cv2.imshow('frame', frame)
      
    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
  
# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()

# read input image
img1 = cv2.imread('color_pencils.jpeg')
img2 = cv2.imread('rainbow.jpeg')

# Scale down to 25%
p = 0.5
w = int(img2.shape[1] * p)
h = int(img2.shape[0] * p)
img2 = cv2.resize(img2, (w, h))

# define range of yellow color in BGR
lower_yellow = np.array([0,100,200])
upper_yellow = np.array([100,255,255])

# Create a mask
mask1 = cv2.inRange(img1, lower_yellow, upper_yellow)
mask2 = cv2.inRange(img2, lower_yellow, upper_yellow)

# Bitwise-AND mask and original image
result1 = cv2.bitwise_and(img1,img1, mask= mask1)
result2 = cv2.bitwise_and(img2,img2, mask= mask2)

# display the mask and masked image
cv2.imshow('Mask',mask1)
cv2.imshow('Masked Image',result1)
cv2.imshow('Mask2',mask2)
cv2.imshow('Masked Image2',result2)
cv2.waitKey(0)
cv2.destroyAllWindows()