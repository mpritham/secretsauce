import os
from flask import Flask, render_template, request
tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
from werkzeug import secure_filename
import pdb

UPLOAD_FOLDER = 'uploads'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def hello():
    print "test"
    x= [Entry("test","test","test"),Entry("test","test","test")]
    print entries[0].title
    pdb.set_trace()
    return render_tsemplate('index.html')

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

class Entry:
    def __init__(self, title, path,description):
        self.title=title
        self.path=path
        self.description=description
#    def getTitle(self):
#        return self.title
#    def getDescription(self):
#        return self.description
#    def getPath(self):
#        return self.path
#        