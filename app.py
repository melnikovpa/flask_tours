from flask import Flask, render_template, abort
from utils.jinja_data import tours, departures

app = Flask(__name__)


@app.route('/')
def index_action():
    return render_template('index.html')


@app.route('/departures/<departure>/')
def departures_action(departure):
    return render_template('departure.html')


@app.route('/tours/<id>/')
def tour_action(id):
    return render_template('tour.html')


@app.route('/data/tours/<int:id>/')
def data_tour(id):
    tour = None
    if id in tours:
        tour = tours[id]

    if tour is None:
        abort(404, "Данные по туру не найдены")

    return render_template('temp_data_tour.html', tour=tour)


@app.route('/data/departures/<departure>')
@app.route('/data/')
def data(departure=""):
    departure_name = departures[departure] if departure != "" and departure in departures else ""
    tours_prepared = {}

    for key, tour in tours.items():
        if departure != "" and tour['departure'] != departure:
            continue

        tours_prepared[key] = tour

    return render_template('temp_data.html', tours=tours_prepared, departure=departure, departure_name=departure_name)


if __name__ == '__main__':
    app.run()
