import os
from flask import Flask, render_template
tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
from werkzeug import secure_filename

UPLOAD_FOLDER = '/uploads'

app = Flask(__name__)
@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/save', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            
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
