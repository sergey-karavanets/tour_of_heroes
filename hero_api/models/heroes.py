from run import db


class Heroes(db.Model):

    def __init__(self, name):
        self.name = name

    __tablename__ = 'heroes'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f'<{self.id}:{self.name}>'

    @classmethod
    def list(cls):
        return cls.query.all()
