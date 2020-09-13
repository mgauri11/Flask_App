
import os
import os,sys
from shutil import copyfile
import cv2
path='C:/Users/Lenovo/Desktop/Portfolio/Gauri.jpg'
filename = os.path.basename(path)
print((filename))
x=copyfile(path, os.path.join("C:/Users/Lenovo/Desktop/Portfolio/Filtered-Image/", filename))
print(x)





dir_path = x
print(dir_path)
ext = '.jpg'
output = 'Beda_02.avi'
#shape = 680, 360 IDEAL TO FIT IN VIDEO TEMPLATE OF WEBSITE
shape = 960, 720
fps = 1
each_image_duration = 5 

images = [f for f in os.listdir(dir_path) if f.endswith(ext)]

fourcc = cv2.VideoWriter_fourcc(*'DIVX')
video = cv2.VideoWriter(output, fourcc, fps, shape)

for _ in range(each_image_duration):

	for image in images:

	    image_path = os.path.join(dir_path, image)
	    image = cv2.imread(image_path)
	    resized=cv2.resize(image,shape) 
	    video.write(resized)

video.release()

clip = moviepy.VideoFileClip("Beda_02.avi")
clip.write_videofile("Beda_02.mp4") 



   



    
    