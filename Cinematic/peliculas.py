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
        ' ORDER BY film DESC'
    ).fetchall()
    return render_template('peliculas/index.html', peliculas=peliculas)

@bp.route('/create', methods=('GET'))

def get_peliculas(id):
    peliculas = get_db().execute(
        'SELECT *'
        ' FROM films'
        ' WHERE film_id = ?',
        (id,)
    ).fetchone()

    if peliculas is None:
        abort(404, f"Post id {id} doesn't exist.")


    return peliculas

@bp.route('/<int:id>/peliculas', methods=('GET'))
def update(id):
    peliculas = get_peliculas(id)
    return render_template('peliculas', peliculas = peliculas)
