import cv2
import numpy as np
# choose codec according to format needed
fourcc = cv2.VideoWriter_fourcc(*'mp4v') 
video=cv2.VideoWriter('video.avi', fourcc, 30,(1280,720))
for j in range(0,972):
   img = cv2.imread('image/'+'image'+str(j)+'.jpg')
   video.write(img)
cv2.destroyAllWindows()
video.release()
