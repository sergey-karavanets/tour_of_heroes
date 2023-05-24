from flask import Flask, jsonify, request

from ..models.heroes import Heroes


class HeroController:
    # app: Flask

    def __init__(self, app):
        self.app = app

    def get_list(self):
        # heroes = Heroes.query.filter().all()
        # return heroes_schema.dump(heroes)
        return []

    # def get_hero(self, hero_id: int):
    #     hero = Heroes.query.get(hero_id)
    #     return hero_schema.dump(hero), 200
    #
    # def search_heroes(self):
    #     name = request.args.get('name', type=str)
    #     heroes = Heroes.query.filter(Heroes.name.ilike("%" + name + "%")).all()
    #     return jsonify(heroes_schema.dump(heroes))
    #
    # def add_hero(self):
    #     new_hero = Heroes(request.json['name'])
    #     db.session.add(new_hero)
    #     db.session.commit()
    #     return hero_schema.dump(new_hero), 201
    #
    # def update_hero(self, hero_id: int):
    #     hero = Heroes.query.get(hero_id)
    #     hero.name = Heroes(request.json['name']).name
    #     db.session.commit()
    #     return jsonify(hero_schema.dump(hero)), 200
    #
    # def delete_hero(self, hero_id: int):
    #     Heroes.query.filter_by(id=hero_id).delete()
    #     db.session.commit()
    #     return "delete successfully", 204
