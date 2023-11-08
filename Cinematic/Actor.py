from flask import (
    Blueprint, flash, g, jsonify, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from Cinematic.db import get_db

bp = Blueprint('actor', __name__,url_prefix="/actor/")
bpapi = Blueprint('api_actores', __name__, url_prefix="/api/actor")


@bp.route('/')
def index():
    db = get_db()
    actores = db.execute(
        'SELECT first_name,last_name,actor_id'
        ' FROM actor '
        ' ORDER BY first_name,last_name '
    ).fetchall()
    return render_template('actor/index.html', actores=actores)

@bpapi.route('/')
def index_api():
    db = get_db()
    actores = db.execute(
        'SELECT first_name,last_name,actor_id'
        ' FROM actor '
        ' ORDER BY first_name,last_name '
    ).fetchall()
    for actor in actores:
        actor["url"] = url_for("api_actores.detalle_api", id=actor["actor_id"], _external=True)
    
    return jsonify(actores=actores)

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

@bp.route("/<int:id>/")
def detalle(id):
    info_del_actor = get_actor(id)
    apariciones = get_actor_de_peliculas(id)
    
    return render_template ('actor/detalle.html', info_del_actor = info_del_actor, apariciones=apariciones)

@bpapi.route("/<int:id>/")
def detalle_api(id):
    info_del_actor = get_actor(id)
    apariciones = get_actor_de_peliculas(id)

    
    return jsonify(info_del_actor = info_del_actor, apariciones=apariciones)

def get_actor_de_peliculas(id):
    actor_pelis = get_db().execute(
    """ SELECT f.film_id, a.actor_id,f.title as peli,a.first_name,a.last_name FROM film f
    JOIN film_actor fa ON f.film_id = fa.film_id
    JOIN actor a on fa.actor_id = a.actor_id
    WHERE a.actor_id = ?""",(id,)).fetchall()  
    for pelicula in actor_pelis:
        pelicula["url"] = url_for("api_peliculas.detalle_api", id=pelicula["film_id"], _external=True)
    
    return actor_pelis






