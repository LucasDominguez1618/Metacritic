from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from Cinematic.db import get_db

bp = Blueprint('idiomas', __name__,url_prefix="/idioma/")

@bp.route('/')
def index():
    db = get_db()
    db.execute(
        'SELECT *'
        ' FROM language '
        ' ORDER BY name '
    )
    idioma= db.fetchall()
    return render_template('idioma/index.html', idioma=idioma)

@bp.route('/create', methods=(['GET']))

def get_idioma(id):
    db = get_db()
    db.execute(
        'SELECT *'
        ' FROM language'
        ' WHERE language_id = %s',
        (id,)
    )
    idioma=db.fetchone()

    if idioma is None:
        abort(404, f"Post id {id} doesn't exist.")


    return idioma


