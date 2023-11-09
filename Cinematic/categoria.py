from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from Cinematic.db import get_db

bp = Blueprint('categorias', __name__,url_prefix="/categoria/")

@bp.route('/')
def index():
    db = get_db()
    db.execute(
        'SELECT *'
        ' FROM category '
        ' ORDER BY name  '
    )
    categorias=db.fetchall()
    return render_template('categoria/index.html', categorias=categorias)

@bp.route('/create', methods=(['GET']))

def get_categoria(id):
    db = get_db()
    db.execute(
        'SELECT *'
        ' FROM film_category'
        'JOIN category'
        ' WHERE category_id = %s',
        (id,)
    )
    categoria=db.fetchone()

    if categoria is None:
        abort(404, f"Post id {id} doesn't exist.")


    return categoria


