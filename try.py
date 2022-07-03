from flask import Flask,render_template,request,abort
from werkzeug.utils import secure_filename
 
app = Flask(__name__)
 
@app.route('/form')
def form():
    return render_template('form.html')
 
@app.route('/upload', methods = ['POST', 'GET'])
def upload():
    if request.method == 'POST':
        if request.files:
            print("gdfjcgasjhdfgs")

            f = request.files['file']
            f.save(secure_filename(f.filename))
            return "File saved successfully"
 
app.run(debug=True)