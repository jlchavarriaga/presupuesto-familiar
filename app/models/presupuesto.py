from app.extensions import db
from datetime import datetime

class Presupuesto(db.Model):
    __tablename__ = 'presupuestos_familiares'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    año = db.Column(db.Integer, nullable=False)
    estado = db.Column(db.String(20), default='activo')
    fecha_creacion = db.Column(db.DateTime, default=datetime.utcnow)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)

    # Relaciones
    periodos = db.relationship('Periodo', backref='presupuesto', lazy=True)

    def __repr__(self):
        return f'<Presupuesto {self.nombre} {self.año}>'
