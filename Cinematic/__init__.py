import os

from flask import Flask, render_template




def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'Cinematic.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/base')
    def hello():
        return render_template("base.html")
    

    from . import db
    db.init_app(app)


    from . import peliculas
    app.register_blueprint(peliculas.bp)
    app.add_url_rule('/', endpoint='index')

    from . import idiomas
    app.register_blueprint(idiomas.bp)
    app.add_url_rule('/', endpoint='index')
    
    from . import Actor
    app.register_blueprint(Actor.bp)
    app.add_url_rule('/', endpoint='index')
    
    from . import categoria
    app.register_blueprint(categoria.bp)
    app.add_url_rule('/', endpoint='index')


    return app        


