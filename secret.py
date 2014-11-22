from flask import Flask, render_template
tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')

@app.route('/')
def hello():
    return render_template('index.html')

if __name__ =="__main__":
    app.run()
class Entry:
    def __init__(self,title, path,description):
        self.title=title
        self.path=path
        self.description=description
    def getTitle():
        return self.title
    def getDescription():
        return self.description
    def getPath():
        return self.path
        
        