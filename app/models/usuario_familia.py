from app.extensions import db

class UsuarioFamilia(db.Model):
    __tablename__ = 'usuarios_familias'

    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), primary_key=True)
    familia_id = db.Column(db.Integer, db.ForeignKey('familias.id'), primary_key=True)
    rol = db.Column(db.String(20), nullable=False, default='miembro')
    fecha_union = db.Column(db.DateTime, default=db.func.now())
