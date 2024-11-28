# models.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Study(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    phase = db.Column(db.String(100))
    sponsor_name = db.Column(db.String(200))

    def __repr__(self):
        return f'<Study {self.name}>'
