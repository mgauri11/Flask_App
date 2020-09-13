from flask import Flask, render_template
from flask import request, redirect, flash
from werkzeug.utils import secure_filename
import os
from PIL import Image, ImageFilter
import cv2
import numpy as np
from shutil import copyfile
import moviepy.editor as moviepy
#from flask_mail import Mail, Message
#from Forms import ContactForm
import sqlite3


 
app = Flask(__name__) 
app.secret_key = 'development key'
 

 
@app.route('/')
def home():
  return render_template('home.html')

@app.route('/about')
def about():
  return render_template('about.html')



PEOPLE_FOLDER = os.path.join('static', 'img')
app.config['IMAGE_UPLOADS'] = PEOPLE_FOLDER

@app.route("/upload-image", methods=["GET", "POST"])
def upload_image():

    if request.method == "POST":

        if request.files:
            
            image = request.files["image"]

            text_00 = request.form['text']

            if (image.filename):
                filename = secure_filename(image.filename)

                full_filename=os.path.join(app.config["IMAGE_UPLOADS"], filename)

                image.save(full_filename)

                print(full_filename)

                im = Image.open(full_filename)
                im_sharp = im.filter( ImageFilter.SHARPEN )
                path='C:/Users/Lenovo/Desktop/Portfolio/flaskapp/app/static/people_photo/trial_01.jpg' 
                im_sharp.save(path)
                f_name=os.path.basename(path)
               
                t=copyfile(path,os.path.join(PEOPLE_FOLDER,f_name))

                dir_path = 'C:/Users/Lenovo/Desktop/Portfolio/flaskapp/app/static/people_photo/'

                ext = '.jpg'
                output = 'Testing1.avi'
                
                shape = 680, 360
                fps = 1
                print(text_00)
                #each_image_duration = 10  #default timer declaration

                images = [f for f in os.listdir(dir_path) if f.endswith(ext)]


                fourcc = cv2.VideoWriter_fourcc(*'DIVX')
                video = cv2.VideoWriter(output, fourcc, fps, shape)

                for _ in range(int(text_00)): #text_00= time for video accepted from the user.

                    for image in images:

                        image_path = os.path.join(dir_path, image)
                        image = cv2.imread(image_path)
                        resized=cv2.resize(image,shape) 
                        video.write(resized)

                video.release()

                clip = moviepy.VideoFileClip("Testing1.avi")
                trial="C:/Users/Lenovo/Desktop/Portfolio/flaskapp/app/static/people_photo/Testing1.mp4"
                x_y=clip.write_videofile(trial)
            
                #.jpg to .avi conversion.
            
                print("Image saved")

                return redirect(request.url)

            else:
                print("That file extension is not allowed")
                return redirect(request.url)

    return render_template("upload_image.html")



#TESTING FOR ANOTHER IMAGE TO VIDEO CONVERSION  ===> AFTER THE IMAGE IS UPLOADED.
PEOPLE_FOLDER1 = os.path.join('static', 'people_photo')
app.config['UPLOAD_FOLDER1'] = PEOPLE_FOLDER1

@app.route('/index', methods=["GET"]) 
def index():
    full_filename = os.path.join(app.config['UPLOAD_FOLDER1'], 'Testing1.mp4')
    return render_template("index.html") 





if __name__ == '__main__':
  app.run(debug=True)