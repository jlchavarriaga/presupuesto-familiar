from app.extensions import db

class Etiqueta(db.Model):
    __tablename__ = 'etiquetas'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    color = db.Column(db.String(7), default='#9b59b6')

    # Clave foránea
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'))

    # Relaciones
    usuario = db.relationship('Usuario', back_populates='etiquetas')
    transacciones = db.relationship('EtiquetaTransaccion', back_populates='etiqueta')
