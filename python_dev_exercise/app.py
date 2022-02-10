from flask import Flask, request, render_template
import csv
import pandas as pd
import webbrowser
from threading import Timer

app = Flask(__name__)

# Read in csv file
df = pd.read_csv('data/patient_tb.csv')
# Delete any duplicate rows
df = df.drop_duplicates(subset=['PatientID', 'MostRecentTestDate', 'TestName'])

# Home page
@app.route('/')
def home():
    return render_template("home.html")

# Search page
@app.route('/search', methods =["GET", "POST"])
def search():
    if request.method == "POST":
       first_name = request.form.get("fname")
       name_df = df[df['PatientFirstName'] == first_name] 
       return render_template('search.html', tables=[name_df.to_html(classes='data', header ="true")], titles=name_df.columns.values)

    return render_template('search.html', tables=[df.to_html(classes='data', header ="true")], titles=df.columns.values)

# Open app in browser on run
def open_app():
      webbrowser.open_new('http://localhost:5000/')

# Main
if __name__ == "__main__":
    Timer(1, open_app).start();
    app.run(port=5000)
