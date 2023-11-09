import psycopg2
import psycopg2.extras
import click
from flask import current_app, g



def get_db():
    if 'db' not in g:
        conn = psycopg2.connect(host="127.0.0.1",
            database="Sakila",
            user="postgres",
            password="postgres",
            port=5432)
        g.db = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        
    return g.db



def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

def init_db():
    db = get_db()

    with current_app.open_resource('BDPeliculas.sql') as f:
        db.executescript(f.read().decode('utf8'))


@click.command('init-db')
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')
def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
