from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello world."

@app.route("/index")
def index():
    title="wanderer"
    return render_template("index.html", title=title)

if __name__ == "__main__":
    app.run()