'''Censoring faces in a video using python'''
import cv2
video=cv2.VideoCapture('sluek.mp4')
success, frame =video.read()
height=frame.shape[0]
width=frame.shape[1]
print(f"w={width},h={height}")
#to recognise face that to be blurred
face_cascade =cv2.CascadeClassifier('faces.xml')
'''output is storing the final video of blurred by giving the exact width and height,
30 represents for continuous 30 frames this format should be applied'''
output=cv2.VideoWriter('blurred_sluek.avi',cv2.VideoWriter_fourcc(*'DIVX'),30,(width,height))
count=0
while success:
    faces =face_cascade.detectMultiScale(frame,1.1,4)
    for (x,y,w,h) in faces:
        '''frames dimensions of a persons face taking x to x+w and y to y+h
        so the below diagram represents x and x+w that is x to x+w area and y to y+h area
        these four combinedly form a box that encloses the target face need to be blurred
                            ----------
                            |        |
                            |        |
                            |_ _ _ _ |
        '''
        frame[y:y+h,x:x+w]=cv2.blur(frame[y:y+h,x:x+w],(50,50))
    output.write(frame)
    success,frame =video.read()
    count+=1
    print(count)
output.release()