from flask import Flask, render_template, request
from get_time_data import getTime

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def search():

    time = getTime()
    return render_template("base.html", time=time)


@app.route("/", methods=["GET"])
def get_data_from_js():
    if request.method == 'GET':
        js_variable = request.form
        print(js_variable)
        return js_variable


@app.after_request
def add_header(response):
    # response.cache_control.no_store = True
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '-1'
    return response


if __name__ == '__main__':
    app.run()
