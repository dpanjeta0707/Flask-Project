#import all the required libraries
from flask import Flask, render_template,request,redirect,url_for, session, g, flash, abort
from bson import ObjectId
import os
import pandas as pd
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource, LabelSet
from bokeh.io import curdoc
from bokeh.embed import components
from bokeh.resources import CDN
import datetime
import charts, creator
from werkzeug.utils import secure_filename


UPLOAD_FOLDER = '/files'

#initiate the flask app
app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


#set static folder
app.static_folder = 'static'

app.secret_key = 'super secret key'
#home page
@app.route('/')
def home():
    return render_template("Home.html")



#register

@app.route('/register')
def register():
    return render_template("Register.html")

#dashboard

@app.route('/humidity', methods = ["GET", "POST"])
def hum():
    p = charts.humidity_plot_full()
    script1, div1 = components(p)

    cdn_js = CDN.js_files[0]
    cdn_css = CDN.css_files

    return render_template("Humidity.html", script1=script1, div1=div1, cdn_css=cdn_css, cdn_js=cdn_js)

@app.route('/temperature')
def temp():
    p2 = charts.temperature_plot_full()
    script2, div2 = components(p2)

    cdn_js = CDN.js_files[0]
    cdn_css = CDN.css_files

    return render_template("Temperature.html", script2=script2, div2=div2, cdn_css=cdn_css, cdn_js=cdn_js)


@app.route('/airflow')
def air():
    
   
    p3=charts.airin_plot_full()
    p4 = charts.airout_plot_full()


    script3, div3 = components(p3)

    script4, div4 = components(p4)



    cdn_js = CDN.js_files[0]
    cdn_css = CDN.css_files



    return render_template("Airflow.html", script3=script3, div3=div3, script4=script4, div4=div4, cdn_css=cdn_css, cdn_js=cdn_js)



@app.route('/material')
def material():
    
    todos=charts.material_plot()

    return render_template("Material.html", todos=todos)


@app.route('/dashboard', methods = ["GET", "POST"])
def dashboard():
    
    p = charts.humidity_plot()
    p2 = charts.temperature_plot()
    p3=charts.airin_plot()
    p4 = charts.airout_plot()

    todos=charts.material_plot()
   



    script1, div1 = components(p)

    script2, div2 = components(p2)

    script3, div3 = components(p3)

    script4, div4 = components(p4)

    



   
    cdn_js = CDN.js_files[0]
    cdn_css = CDN.css_files



    return render_template("Dashboard.html", todos=todos, script1=script1, div1=div1, script2=script2, div2=div2, script3=script3, div3=div3, script4=script4, div4=div4, cdn_css=cdn_css, cdn_js=cdn_js)


#upload

@app.route('/write', methods = ["GET", "POST"]) 
def write():
    return render_template("Write.html", value="Submit")


@app.route('/written', methods = ["GET", "POST"]) 
def written():
    if request.method =='POST':
        start_date = request.form.get("date")
        end_date = request.form.get("date-1")
        c_lot = request.form.get("text")
        l_lot = request.form.get("text-1")
        p_lot = request.form.get("text-2")
        t_formula = request.form.get("select")
        creator.material_append(start_date, end_date, c_lot, l_lot, p_lot, t_formula)
        return render_template("Material.html")

 
@app.route('/upload')
def upload():
    return render_template("Upload.html", value1 = "Upload", value2 = "Upload", value3 = "Upload")


@app.route('/th_upload', methods = ["GET","POST"]) 
def uploadth():
    if request.method == 'POST':
        if request.files:
            file=request.files['file']
            creator.temphum_append(file)
            
        return render_template("Upload.html",value1 = "Uploaded", value2 = "Upload", value3 = "Upload")


@app.route('/airin_upload', methods = ["GET","POST"]) 
def uploadairin():
    if request.method == 'POST':
        if request.files:
            file=request.files['file']
            creator.airin_append(file)
            
        return render_template("Upload.html",value1 = "Upload", value2 = "Uploaded", value3 = "Upload")            


@app.route('/airout_upload', methods = ["GET","POST"]) 
def uploadairout():
    if request.method == 'POST':
        if request.files:
            file=request.files['file']
            creator.airout_append(file)
            
        return render_template("Upload.html", value1 = "Upload", value2 = "Upload", value3 = "Uploaded")
#about

@app.route('/about')
def about():
    return render_template("About.html")


#contacts

@app.route('/contact')
def contact():
    return render_template("Contact.html")






if __name__ == '__main__':
    app.run(debug=True)