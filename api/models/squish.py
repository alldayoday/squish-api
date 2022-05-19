from datetime import datetime
from api.models.db import db

class Squish(db.Model):
    __tablename__ = 'squishs'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    desc = db.Column(db.String(250))
    sizes = db.Column(db.String(250))
    cat = db.Column(db.String(250))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    profile_id = db.Column(db.Integer, db.ForeignKey('profiles.id'))

    def __repr__(self):
      return f"Cat('{self.id}', '{self.name}'"

    def serialize(self):
      cat = {c.name: getattr(self, c.name) for c in self.__table__.columns}
      return cat