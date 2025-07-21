from app.extensions import db

class PlanPago(db.Model):
    __tablename__ = 'planes_pago'

    id = db.Column(db.Integer, primary_key=True)
    monto = db.Column(db.Numeric(12, 2), nullable=False)
    porcentaje = db.Column(db.Numeric(5, 2))
    fecha_esperada = db.Column(db.Date, nullable=False)
    estado = db.Column(db.String(20), default='pendiente')

    # Claves foráneas
    deuda_id = db.Column(db.Integer, db.ForeignKey('deudas.id'))
    transaccion_id = db.Column(db.Integer, db.ForeignKey('transacciones.id'))

    # Relación con Transaccion es opcional (solo cuando se pague)
