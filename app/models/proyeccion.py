from app.extensions import db
from enum import Enum

class TipoProyeccion(Enum):
    INGRESO = 'ingreso'
    GASTO = 'gasto'

class Proyeccion(db.Model):
    __tablename__ = 'proyecciones'

    id = db.Column(db.Integer, primary_key=True)
    monto = db.Column(db.Numeric(12, 2), nullable=False)
    tipo = db.Column(db.Enum(TipoProyeccion), nullable=False)
    es_automatico = db.Column(db.Boolean, default=True)
    descripcion = db.Column(db.Text)

    # Claves foráneas
    periodo_id = db.Column(db.Integer, db.ForeignKey('periodos.id'))
    ingreso_id = db.Column(db.Integer, db.ForeignKey('ingresos.id'))
    gasto_id = db.Column(db.Integer, db.ForeignKey('gastos.id'))

    # Relaciones
    periodo = db.relationship('Periodo', backref='proyecciones')
    ingreso = db.relationship('Ingreso', backref='proyecciones')
    gasto = db.relationship('Gasto', backref='proyecciones')

