from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/bio', methods=['GET'])
def bio():
    return render_template('bio.html')

@app.route('/photos', methods=['GET'])
def photos():
    return render_template('photos.html')

@app.route('/cv', methods=['GET'])
def cv():
    return render_template('cv.html')

@app.route('/awards', methods=['GET'])
def awards():
    return render_template('awards.html')

app.run()
