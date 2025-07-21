from app.extensions import db

class EtiquetaTransaccion(db.Model):
    __tablename__ = 'etiquetas_transacciones'

    transaccion_id = db.Column(db.Integer, db.ForeignKey('transacciones.id'), primary_key=True)
    etiqueta_id = db.Column(db.Integer, db.ForeignKey('etiquetas.id'), primary_key=True)

    # Relaciones
    transaccion = db.relationship('Transaccion', back_populates='etiquetas')
    etiqueta = db.relationship('Etiqueta', back_populates='transacciones')
