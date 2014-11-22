import os
from flask import Flask, render_template, request, Response
from werkzeug import secure_filename
from models import Entry
import pdb

def parse_files():
    entries=[]
    for dirname, dirnames, filenames in os.walk('static/uploads/'):
    # print path to all subdirectories firs
        for subdirname in dirnames:
            print os.path.join(dirname, subdirname)

    # print path to all filenames.
        for filename in filenames:
            directory =os.path.join(dirname, filename)

            entries.append(Entry(filename, directory, "Some description"))
    return entries


tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
UPLOAD_FOLDER = 'static/uploads'

#Entries dict
entries = []

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
parse_files()
@app.route('/')
def hello():
    entries=parse_files()
    return render_template('index2.html',static_folder='static/',entries=entries,isImage=isImage)

@app.route('/save', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        title=request.form['title']
        file = request.files['file']
        if file:
            filename = secure_filename(file.filename)
            filePath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            entries.append(Entry(filename, filePath, "Some Description"))
            file.save(filePath)
        return "Thank you come again"

@app.route('/getFile/<file>', methods=['GET'])
def getFile(file):
    return Response(open('static/uploads/' + file),
                       mimetype="multipart/mixed",
                       headers={"Content-Disposition":
                                    "attachment;filename=" + file})
def isImage(entry):
    #pdb.set_trace()
    extension=os.path.splitext(entry.path)[1]
    if(extension==".png"or extension==".jpg" or extension==".jpeg"):
        return True
    else:
        return False
if __name__ == "__main__":
    app.run()
