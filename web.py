from flask import Flask, render_template

Web = Flask(__name__)

@Web.route("/")
def Home():
    return render_template("index.html")

if __name__ == "__main__":
    Web.run()