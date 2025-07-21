from app.extensions import db

class Adjunto(db.Model):
    __tablename__ = 'adjuntos'

    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(20), nullable=False)
    url = db.Column(db.String(255), nullable=False)
    nombre_archivo = db.Column(db.String(100), nullable=False)
    fecha_subida = db.Column(db.DateTime, server_default=db.func.now())

    # Clave foránea
    transaccion_id = db.Column(db.Integer, db.ForeignKey('transacciones.id'))

    # Relación
    transaccion = db.relationship('Transaccion', back_populates='adjuntos')
