from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/<name>")
def user(name):
    return render_template("test2.html",content=name)

@app.route("/test")
def test():
    return render_template("test3.html")

@app.route("/list")
def test_list():
    return render_template("test4.html",content=['utkarsh','aakriti','oscar','dhruv'])
if __name__ == "__main__":
    app.run()
