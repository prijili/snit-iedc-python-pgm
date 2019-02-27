from flask import Flask,render_template

app=Flask(__name__)

@app.route("/")
def index():
    return  render_template("index.html")
@app.route("/home")
def home():
    return render_template("mca.html")

@app.route("/about")
def about():
    return "fantastic atmosphere"

@app.route("/contact")
def contact():
    return "my no is 75945523...."
if(__name__=="__main__"):
    app.run(debug=True)