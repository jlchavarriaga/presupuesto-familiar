from app.extensions import db
from enum import Enum

class TipoTransaccion(Enum):
    GASTO = 'gasto'
    INGRESO = 'ingreso'
    PAGO_DEUDA = 'pago_deuda'

class Transaccion(db.Model):
    __tablename__ = 'transacciones'

    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.Enum(TipoTransaccion), nullable=False)
    monto = db.Column(db.Numeric(12, 2), nullable=False)
    fecha = db.Column(db.Date, nullable=False)
    descripcion = db.Column(db.Text)

    # Claves foráneas
    periodo_id = db.Column(db.Integer, db.ForeignKey('periodos.id'))
    gasto_id = db.Column(db.Integer, db.ForeignKey('gastos.id'))
    ingreso_id = db.Column(db.Integer, db.ForeignKey('ingresos.id'))
    deuda_id = db.Column(db.Integer, db.ForeignKey('deudas.id'))

    # Relaciones
    periodo = db.relationship('Periodo', back_populates='transacciones')
    gasto = db.relationship('Gasto', back_populates='transacciones')
    adjuntos = db.relationship('Adjunto', back_populates='transaccion', cascade='all, delete-orphan')
    etiquetas = db.relationship('EtiquetaTransaccion', back_populates='transaccion')
