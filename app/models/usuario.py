from app.extensions import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class Usuario(db.Model, UserMixin):
    __tablename__ = 'usuarios'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256))
    nombre = db.Column(db.String(80), nullable=False)
    avatar = db.Column(db.String(255))
    fecha_creacion = db.Column(db.DateTime, server_default=db.func.now())

    # Relaciones
    familias = db.relationship('UsuarioFamilia', back_populates='usuario', cascade='all, delete-orphan')
    presupuestos_creados = db.relationship('Presupuesto', back_populates='creador')
    categorias_gastos = db.relationship('CategoriaGasto', back_populates='usuario')
    categorias_ingresos = db.relationship('CategoriaIngreso', back_populates='usuario')
    etiquetas = db.relationship('Etiqueta', back_populates='usuario')

    def __repr__(self):
        return f'<Usuario {self.email}>'

    @property
    def password(self):
        raise AttributeError('La contraseña no es legible')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verificar_password(self, password):
        return check_password_hash(self.password_hash, password)

@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))
