from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('categorias', __name__,url_prefix="/categoria/")

@bp.route('/')
def index():
    db = get_db()
    categorias = db.execute(
        'SELECT *'
        ' FROM category '
        ' ORDER BY name  '
    ).fetchall()
    return render_template('categoria/index.html', categorias=categorias)

@bp.route('/create', methods=(['GET']))

def get_categoria(id):
    categoria = get_db().execute(
        'SELECT *'
        ' FROM film_category'
        'JOIN category'
        ' WHERE category_id = ?',
        (id,)
    ).fetchone()

    if categoria is None:
        abort(404, f"Post id {id} doesn't exist.")


    return categoria


