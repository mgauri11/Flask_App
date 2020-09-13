import os
import os,sys
from shutil import copyfile
import cv2
import moviepy.editor as moviepy

dir_path = 'C:/Users/DomainTest/02-01-2020/python-database/contact-us(flask)/flaskapp/app/static/people_photo/'

#print(dir_path)
ext = '.jpg'
output = 'Beda.avi'
#shape = 680, 360 IDEAL TO FIT IN VIDEO TEMPLATE OF WEBSITE
shape = 680, 360
fps = 1
each_image_duration = 15 

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

clip = moviepy.VideoFileClip("Beda.avi")
clip.write_videofile("C:/Users/DomainTest/02-01-2020/python-database/contact-us(flask)/flaskapp/app/static/people_photo/Beda_02.mp4") 