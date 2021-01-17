from flask import Flask, render_template, request
from get_time_data import get_time

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def search():

    time = get_time()
    return render_template("base.html", time=time)


if __name__ == '__main__':
    app.run()
