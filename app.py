from flask import Flask, request, Response, redirect, url_for
from flask_restful import Resource, Api, reqparse
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/tour_of_heroes'
db = SQLAlchemy(app)
ma = Marshmallow(app)
api = Api(app)


class Heroes(db.Model):

    __tablename__ = 'heroes'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f'<{self.id}:{self.name}>'


class HeroesSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name')

    links = ma.Hyperlinks({
        'self': ma.URLFor('book_detail', values=dict(id='<id>')),
        'collection': ma.URLFor('book_list')
    })


hero_schema = HeroesSchema()
heroes_schema = HeroesSchema(many=True)


@app.route('/api/heroes', methods=['GET'])
def get_heroes():
    data = db.select(Heroes).order_by(Heroes.id)
    heroes = db.session.execute(data).scalars()
    return heroes_schema.dump(heroes)


@app.route('/api/detail/<int:id>', methods=['GET'])
def get_hero(id):
    hero = db.get_or_404(Heroes, id)
    return hero_schema.dump(hero)


@app.route('/api/add_hero', methods=['POST'])
def create_hero():
    hero = Heroes(
        id=request.json['id'],
        name=request.json['name']
    )
    db.session.add(hero)
    db.session.commit()
    return Response(status=201)


@app.route('/api/detail/<int:id>', methods=['PATCH'])
def update_hero(id):
    hero = db.get_or_404(Heroes, id)
    new_name = request.json['name']
    hero.name = new_name
    db.session.commit()
    return Response(status=200)


@app.route('/api/detail/<int:id>', methods=['DELETE'])
def delete_hero(id):
    hero = db.get_or_404(Heroes, id)
    db.session.delete(hero)
    db.session.commit()
    return Response(status=200)


@app.route('/api/search/<search_term>')
def search_hero(search_term):
    heroes = Heroes.query.filter(Heroes.name.like('%'+search_term+'%')).order_by(Heroes.id).all()
    return heroes_schema.dump(heroes)


if __name__ == '__main__':
    app.run(debug=True)
