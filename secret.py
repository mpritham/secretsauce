import os
from flask import Flask, render_template, request
from werkzeug import secure_filename
from models import Entry
import pdb

tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
UPLOAD_FOLDER = 'static/uploads'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def hello():
    print "test"
    entries= [Entry("meow","static/uploads/download.jpg","test")]
    return render_template('index.html',static_folder='templates/',entries=entries)

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


# class Entry:
#     def __init__(self, title, path,description):
#         self.title=title
#         self.path=path
#         self.description=description
#    def getTitle(self):
#        return self.title
#    def getDescription(self):
#        return self.description
#    def getPath(self):
#        return self.path
#        