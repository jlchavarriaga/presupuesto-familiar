from app.extensions import db

class Familia(db.Model):
    __tablename__ = 'familias'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    codigo_invitacion = db.Column(db.String(50), unique=True)
    fecha_creacion = db.Column(db.DateTime, default=db.func.now())

    # Relaciones
    miembros = db.relationship('UsuarioFamilia', backref='familia', cascade='all, delete-orphan')
    presupuestos = db.relationship('Presupuesto', backref='familia', lazy=True)
