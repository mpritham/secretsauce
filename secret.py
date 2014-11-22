import os
from flask import Flask, render_template, request, Response
from werkzeug import secure_filename
from models import Entry
import pdb

tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
UPLOAD_FOLDER = 'uploads'

#Entries dict
entries = []

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def hello():
    entries.append(Entry("meow","test","test"))
    return render_template('index.html', entries=entries)

@app.route('/save', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filename = secure_filename(file.filename)
            filePath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            entries.append(Entry(filename, filePath, "Some Description"))
            file.save(filePath)
            return "Thanks for uploading"
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''
@app.route('/getFile', methods=['GET'])
def get():
    return Response(open('uploads/test.c'),
                       mimetype="multipart/mixed",
                       headers={"Content-Disposition":
                                    "attachment;filename="+"test.c"})

if __name__ == "__main__":
    app.run()