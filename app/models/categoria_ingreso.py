from app.extensions import db


class CategoriaIngreso(db.Model):
    __tablename__ = 'categorias_ingresos'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    descripcion = db.Column(db.Text)
    icono = db.Column(db.String(50))
    color = db.Column(db.String(7), default='#2ecc71')

    # Clave foránea
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'))

    # Relaciones
    usuario = db.relationship('Usuario', back_populates='categorias_ingresos')
    ingresos = db.relationship('Ingreso', back_populates='categoria')
