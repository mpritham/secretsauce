from flask import Flask, render_template
tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')

@app.route('/')
def hello():
    return render_template('index.html')

if __name__ =="__main__":
    app.run()
