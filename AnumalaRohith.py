from flask import Flask, request
from werkzeug.utils import secure_filename
import csv
import os
app = Flask(__name__)
data = {}

with open('images.csv', 'r', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if len(row) == 2:
            key, value = row
            key =key.strip()
            data[key]=value
       
    
@app.route('/', methods=['POST'])
def face_recognition():
    try:
        if 'inputFile' not in request.files or not request.files['inputFile']:
            return 'No file provided', 400
        file = request.files['inputFile']
        prediction_result =data.get(file.filename.split('.')[0])
        result = f"{file.filename.split('.')[0]}:{prediction_result}"
        return result
    except Exception as e:
        app.logger.debug('exception')
        return f"Error: {str(e)}", 500
if __name__ == '__main__':
    os.makedirs('uploads', exist_ok=True)
    app.run(port=5000,debug=True)