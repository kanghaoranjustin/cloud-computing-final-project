from image_classification_model import get_image_class
from flask import Flask, request
import codecs

app = Flask(__name__)

@app.route("/")
def homepage():
    file = codecs.open("home.html", "r", "utf-8")
    return file.read()

@app.route("/result", methods=["POST"])
def result():
    image_link = request.form["image_link"]
    image_class, img_path = get_image_class(image_link)
    return "<h1>Your Image Class is:</h1><br>" + image_class + "<br>" + "<img src='"+ img_path +"'>"

if __name__ == "__main__":
    app.run()