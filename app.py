from flask import Flask, flash, request, redirect, jsonify
from werkzeug.utils import secure_filename
from flask_cors import CORS
import utils

app = Flask(__name__)
app.secret_key = 'python_app_secret_key'

CORS(app)

def get_extension(filename):
    return filename.rsplit('.', 1)[1].lower()

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
def allowed_file(filename):
    return '.' in filename and get_extension(filename) in ALLOWED_EXTENSIONS

def save_file(img_file):
    filename = secure_filename(img_file.filename)
    file_path = 'images/main.' + get_extension(filename)
    img_file.save(file_path)
    return file_path

@app.route('/', methods = ['GET', 'POST'])
def process_image():
    if request.method == 'GET':
        return 'Hello from get method!'

    if 'image' not in request.files:
        flash('No file part')
        redirect(request.url)

    img_file = request.files['image']

    if img_file.filename == '':
        flash('No selected file')
        redirect(request.url)

    if not allowed_file(img_file.filename):
        flash('Invalid file type')
        redirect(request.url)

    file_path = save_file(img_file)

    area, number = utils.detect_and_extract_lp_text(file_path)

    data = {
        'area': area,
        'number': number,
    }

    response = jsonify(data)
    response.headers['Content-Type'] = 'application/json; charset=utf-8'

    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3001, debug=True)
