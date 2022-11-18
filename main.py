import os
from flask import Flask, render_template, request

from places import get_places_table

app = Flask(__name__)
app.config['SECRET_KEY'] = f'{os.urandom(12)}'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        location = request.form['location']
        radius = request.form['radius']
        keyword = request.form['keyword']
        limit = request.form['limit']

        return f'<center>{get_places_table(place_coordinates=location, place_radius=radius, keyword=keyword, limit=limit)}</center> '

    return render_template('index.html')


if __name__ == '__main__':
    app.run()
