from app.extensions import db

class Periodo(db.Model):
    __tablename__ = 'periodos'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    fecha_inicio = db.Column(db.Date)
    fecha_fin = db.Column(db.Date)
    presupuesto_id = db.Column(db.Integer, db.ForeignKey('presupuestos_familiares.id'))

    def __repr__(self):
        return f'<Periodo {self.nombre}>'