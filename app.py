from flask import Flask, render_template, request
from get_time_data import get_time
from form import WordSearchForm
from weather_geolocation import get_weather_info

app = Flask(__name__)

app.config['SECRET_KEY'] = 'kjhsdfkgjh345toisufg980sd7g2l34khasd987asdfk'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


@app.route("/", methods=["GET", "POST"])
def search():
    form = WordSearchForm()
    time = get_time()
    if form.validate_on_submit() and request.form['word_search'].strip():
        query = request.form['word_search']
        weather_json = get_weather_info(query.lower())
        temp = str(weather_json['main']['temp']) + '°C'
        icon_value = weather_json['weather'][0]['icon']
        weather_image = "http://openweathermap.org/img/wn/" + icon_value + "@2x.png"
        return render_template("base.html", data=query.lower(),
                               form=form, temp=temp,
                               city=weather_json['name'], cloud=weather_json['weather'][0]['description'].title(),
                               time=time, icon=weather_image)

    return render_template("base.html", form=form, time=time)


@app.after_request
def add_header(response):
    # response.cache_control.no_store = True
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '-1'
    return response


if __name__ == '__main__':
    app.run()
