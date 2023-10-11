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
        abort(404, f"Esa Pelicula {id} no existe.")


    return pelicula

def get_movie(id):
    movie = get_db().execute(
    """ SELECT f.film_id,f.release_year as año_de_lanzamiento,
    a.first_name,a.last_name,c.name as categoria FROM film f 
    JOIN film_category fc ON f.film_id = fc.film_id
    JOIN category c ON fc.category_id = c.category_id
    JOIN film_actor fa ON f.film_id = fa.film_id
    JOIN actor a ON fa.actor_id = a.actor_id  
    WHERE f.film_id = ?""",(id,)
    ).fetchone()
    return movie
def get_language(id):
    language = get_db().execute(
    """ SELECT f.film_id, l.name as idioma FROM film f 
    JOIN language l ON f.language_id = l.language_id
    WHERE f.film_id = ?""",(id,)
    ).fetchone()
    return language


def get_actor(id):
    actors = get_db().execute(
    """ SELECT f.film_id, a.actor_id,a.first_name as nombre,a.last_name as apellido FROM film f     
    JOIN film_actor fa ON f.film_id = fa.film_id
    JOIN actor a ON fa.actor_id = a.actor_id  
    WHERE f.film_id = ?""",(id,)
    ).fetchall()

    return actors


@bp.route ("/detalle/<int:id>/")
def detalle(id):
    movie_info = get_movie(id)
    actor_info = get_actor(id)
    language_info = get_language(id)
    return render_template ('peliculas/detalle.html',movie_info =movie_info, actor_info = actor_info,language_info = language_info)




