from flask import Flask, render_template, request, redirect, url_for
import os
from vehicle_detect import detect_vehicles

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        video = request.files['video']
        if video:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], video.filename)
            video.save(filepath)

            # Run detection
            result_path, count = detect_vehicles(filepath)

            return render_template('index.html', result_path=result_path, count=count)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
