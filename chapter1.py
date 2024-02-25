# 1 Read images, videos, webcam 

import cv2
print('Package imported')


# working with Images 

# img = cv2.imread('Resources/pikachu.jpg')
# cv2.imshow('Output',img)
# # cv2.waitKey(0) #infinite delay
# cv2.waitKey(5000) #waits for 5 sec



# importing video 

# vid = cv2.VideoCapture('Resources/Beach.mp4')

# while True:
#     success, img =  vid.read()
#     cv2.imshow('Video',img)
    
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
    


# Webcam 

cam = cv2.VideoCapture(0)
cam.set(3,640)
cam.set(4,480)
cam.set(10,100)


while True:
    success, img = cam.read()
    cv2.imshow('Video',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break