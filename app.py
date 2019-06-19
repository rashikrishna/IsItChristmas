from flask import Flask,render_template
import datetime

app=Flask(__name__)
@app.route("/")
def index():
    now=datetime.datetime.now()
    christmas=now.month==12 and now.day==25
    return render_template("/home/rashi/Christmas/index.html",christmas=christmas)

if (__name__=="__main__"):
     app.run(port=5001)
