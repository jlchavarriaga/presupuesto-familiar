from app.extensions import db


class Ingreso(db.Model):
    __tablename__ = 'ingresos'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    monto = db.Column(db.Numeric(12, 2), nullable=False)
    periodicidad = db.Column(db.String(20), nullable=False)
    fecha_inicio = db.Column(db.Date, nullable=False)
    fecha_fin = db.Column(db.Date)
    descripcion = db.Column(db.Text)

    # Claves foráneas
    categoria_id = db.Column(db.Integer, db.ForeignKey('categorias_ingresos.id'))
    presupuesto_id = db.Column(db.Integer, db.ForeignKey('presupuestos_familiares.id'))

    # Relaciones
    categoria = db.relationship('CategoriaIngreso', back_populates='ingresos')
    presupuesto = db.relationship('Presupuesto')
    proyecciones = db.relationship('Proyeccion', back_populates='ingreso')
    transacciones = db.relationship('Transaccion', back_populates='ingreso')
