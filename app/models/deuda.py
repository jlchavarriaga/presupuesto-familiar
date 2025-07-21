from app.extensions import db

class Deuda(db.Model):
    __tablename__ = 'deudas'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    monto_total = db.Column(db.Numeric(12, 2), nullable=False)
    monto_pendiente = db.Column(db.Numeric(12, 2), nullable=False)
    tasa_interes = db.Column(db.Numeric(5, 2), default=0)
    fecha_inicio = db.Column(db.Date, nullable=False)
    fecha_fin = db.Column(db.Date)
    descripcion = db.Column(db.Text)

    # Claves foráneas
    presupuesto_id = db.Column(db.Integer, db.ForeignKey('presupuestos_familiares.id'))
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'))

    # Relaciones
    presupuesto = db.relationship('Presupuesto', backref='deudas')
    usuario = db.relationship('Usuario', backref='deudas')
    planes_pago = db.relationship('PlanPago', backref='deuda', cascade='all, delete-orphan')
    transacciones = db.relationship('Transaccion', backref='deuda')
