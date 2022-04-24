import cv2 as cv

# Reading Images 

# img = cv.imread('./Images/client.jpg') # Reads the image in BGR format
# cv.imshow('client', img) # Shows the image
# For images
# cv.waitKey(0) # Waits for a key press


# Reading Video
capture = cv.VideoCapture('./Videos/TomoSAR.mp4') # 0 is the default camera
while True:
    ret, frame = capture.read() # ret is boolean, frame is the image
    cv.imshow('Video', frame) # Show the image
    if cv.waitKey(20) & 0xFF == ord('q'): # Press q to quit
        break

capture.release() # Releases the camera
cv.destroyAllWindows() # Closes all the windows


#Resizing and Rescaling the Images

