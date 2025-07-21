# app\__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate

# Inicialización de extensiones
db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()

def crear_aplicacion():
    """Factory principal para crear la aplicación Flask"""
    app = Flask(__name__)

    # Configuración
    app.config.from_object('app.config.Config')

    # Inicializar extensiones
    inicializar_extensiones(app)

    # Registrar blueprints
    registrar_blueprints(app)

    # Configurar contexto para shell
    configurar_shell_context(app)

    return app

def inicializar_extensiones(app):
    """Inicializa todas las extensiones Flask"""
    db.init_app(app)
    migrate.init_app(app, db)

    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    login_manager.login_message = 'Por favor inicia sesión para acceder a esta página'
    login_manager.login_message_category = 'info'

def registrar_blueprints(app):
    """Registra todos los blueprints de la aplicación"""
    from app.routes.auth import auth_bp
    from app.routes.presupuestos import presupuestos_bp
    from app.routes.familias import familias_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(presupuestos_bp, url_prefix='/presupuestos')
    app.register_blueprint(familias_bp, url_prefix='/familias')

def configurar_shell_context(app):
    """Añade modelos al contexto de Flask shell"""
    @app.shell_context_processor
    def contexto_shell():
        from app.models import Usuario, Familia, Presupuesto
        return {
            'db': db,
            'Usuario': Usuario,
            'Familia': Familia,
            'Presupuesto': Presupuesto
        }

