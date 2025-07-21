from app.extensions import db

class CategoriaGasto(db.Model):
    __tablename__ = 'categorias_gastos'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    descripcion = db.Column(db.Text)
    icono = db.Column(db.String(50))
    color = db.Column(db.String(7), default='#3498db')

    # Clave foránea
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'))

    # Relaciones
    usuario = db.relationship('Usuario', back_populates='categorias_gastos')
    gastos = db.relationship('Gasto', back_populates='categoria')
