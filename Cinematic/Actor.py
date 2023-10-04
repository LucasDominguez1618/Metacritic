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


