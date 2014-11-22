import os
from flask import Flask, render_template, request
from werkzeug import secure_filename
from models import Entry
import pdb

def parse_files():
    entries=[]
    for dirname, dirnames, filenames in os.walk('static/uploads/'):
    # print path to all subdirectories first.
        for subdirname in dirnames:
            print os.path.join(dirname, subdirname)

    # print path to all filenames.
        for filename in filenames:
            directory =os.path.join(dirname, filename)
            entries.append(Entry(filename,directory,"Some description"))
    return entries
    

tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
UPLOAD_FOLDER = 'static/uploads'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
parse_files()
@app.route('/')
def hello():
    entries=parse_files()
    return render_template('index.html',static_folder='static/',entries=entries)


@app.route('/save', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return "TEST" 
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''

if __name__ =="__main__":
    app.run()
    

