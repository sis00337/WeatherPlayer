from flask import Flask, render_template, request
from get_time_data import get_time

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def search():

    time = get_time()
    return render_template("base.html", time=time)


@app.after_request
def add_header(response):
    # response.cache_control.no_store = True
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '-1'
    return response


if __name__ == '__main__':
    app.run()
