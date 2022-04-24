import cv2 as cv

# Reading Images 

img = cv.imread('./Images/client.jpg') # Reads the image in BGR format
cv.imshow('client', img) # Shows the image

def ChangeRes(height, width):
    #live video only
    capture.setwidth(3, width)
    capture.setheight(4, height)



def rescale(frame, scale=0.75):
    # This will work for images, videos, live video
    width = int(frame.shape[1] * scale) # Width of the image
    height = int(frame.shape[0] * scale)    # Height of the image

    dim = (width, height) # Dimensions of the image

    return cv.resize(frame, dim, interpolation = cv.INTER_AREA) # Rescales the image

# Rescaling Image
rescale_image = rescale(img, scale=0.2)
cv.imshow('rescale', rescale_image)
cv.waitKey(0)

# Rescaling Video
capture = cv.VideoCapture('./Videos/TomoSAR.mp4') # 0 is the default camera
while True:
    ret, frame = capture.read() # ret is boolean, frame is the image
    frame_resized = rescale(frame) # Rescales the image

    # cv.imshow('Video', frame_resized) # Show the image
    cv.imshow('Video', frame) # Show the image
    if cv.waitKey(20) & 0xFF == ord('q'): # Press q to quit
        break

capture.release() # Releases the camera
cv.destroyAllWindows() # Closes all the windows

