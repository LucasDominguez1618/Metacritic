from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('peliculas', __name__)

@bp.route('/')
def index():
    db = get_db()
    peliculas = db.execute(
        'SELECT *'
        ' FROM film '
        ' ORDER BY title'
    ).fetchall()
    return render_template('peliculas/index.html', peliculas=peliculas)

@bp.route('/create', methods=(['GET']))

def get_pelicula(id):
    pelicula = get_db().execute(
        'SELECT *'
        ' FROM film'
        ' WHERE film_id = ?',
        (id,)
    ).fetchone()

    if pelicula is None:
        abort(404, f"Post id {id} doesn't exist.")


    return pelicula

@bp.route('/<int:id>/detalle', methods=(['GET']))
def update(id):
    pelicula = get_pelicula(id)
    return render_template('detalle', pelicula = pelicula)






