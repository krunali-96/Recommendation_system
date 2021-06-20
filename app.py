from flask import Flask, request, render_template
from model import getStartup

app = Flask(__name__)

@app.route("/", methods=["GET"])
def base():
    return render_template("base.html")

@app.route("/home", methods=["GET"])
def home():
    return render_template("home.html")

@app.route("/recommend", methods=["GET", "POST"])
def recommend():
    if request.method == "POST":
        name = request.form.get("name", None)
        startup_list, found = getStartup(name)
        return render_template("recommend.html", found=found, startup_table=startup_list)

if __name__=="__main__":
    app.run(debug=True)
