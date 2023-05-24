from marshmallow import Schema, fields


class HeroesSchema(Schema):
    class Meta:
        fields = ('id', 'name')

    id = fields.Integer(required=True)
    name = fields.String(required=True)


hero_schema = HeroesSchema()
heroes_schema = HeroesSchema(many=True)
