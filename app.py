from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/tour_of_heroes'
db = SQLAlchemy(app)


class Heroes(db.Model):
    __tablename__ = 'heroes'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f'<{self.id}:{self.name}>'


@app.route('/')
def index():
    return 'Hello World'


if __name__ == '__main__':
    app.run(debug=True)
