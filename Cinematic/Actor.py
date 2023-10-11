from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('actores', __name__,url_prefix="/actor/")

@bp.route('/')
def index():
    db = get_db()
    actores = db.execute(
        'SELECT *'
        ' FROM actor '
        ' ORDER BY first_name,last_name '
    ).fetchall()
    return render_template('actor/index.html', actores=actores)

@bp.route('/create', methods=(['GET']))

def get_actor(id):
    actor = get_db().execute(
        'SELECT *'
        ' FROM actor'
        ' WHERE actor_id = ?',
        (id,)
    ).fetchone()

    if actor is None:
        abort(404, f"Post id {id} doesn't exist.")


    return actor


def get_actor(id):
    actor = get_db().execute(
    """ SELECT a.actor_id,a.first_name,a.last_name,c.name as categoria FROM film f 
    JOIN film_category fc ON f.film_id = fc.film_id
    JOIN category c ON fc.category_id = c.category_id
    JOIN film_actor fa ON f.film_id = fa.film_id
    JOIN actor a ON fa.actor_id = a.actor_id  
    WHERE f.film_id = ?""",(id,)
    ).fetchone()

    return actor
@bp.route ("/detalle/<int:id>/")
def detalle(id):
    actor_info = get_actor(id)
    return render_template ('peliculas/detalle.html',actor_info =actor_info)




