
from flask import request, redirect
from werkzeug.utils import secure_filename

import os

#app.config["IMAGE_UPLOADS"] = "/mnt/c/wsl/projects/pythonise/tutorials/flask_series/app/app/static/img/uploads"
PEOPLE_FOLDER = os.path.join('static', 'img')
app.config['IMAGE_UPLOADS'] = PEOPLE_FOLDER
app.config["ALLOWED_IMAGE_EXTENSIONS"] = ["JPEG", "JPG", "PNG", "GIF"]


def allowed_image(filename):

    if not "." in filename:
        return False

    ext = filename.rsplit(".", 1)[1]

    if ext.upper() in app.config["ALLOWED_IMAGE_EXTENSIONS"]:
        return True
    else:
        return False




@app.route("/upload-image", methods=["GET", "POST"])
def upload_image():

    if request.method == "POST":

        if request.files:
            
            image = request.files["image"]

            if image.filename == "":
                print("No filename")
                return redirect(request.url)

            if allowed_image(image.filename):
                filename = secure_filename(image.filename)

                image.save(os.path.join(app.config["IMAGE_UPLOADS"], filename))

                print("Image saved")

                return redirect(request.url)

            else:
                print("That file extension is not allowed")
                return redirect(request.url)

    return render_template("upload_image.html")