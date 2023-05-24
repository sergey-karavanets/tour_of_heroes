import importlib

import connexion
from connexion import Resolver
from flask import Blueprint, Flask
from jinja2 import FileSystemLoader, Environment
from swagger_ui_bundle import swagger_ui_3_path


class Heroes(Resolver):
    def __init__(self, app: Flask):
        super().__init__()
        self.app = app

    def resolve_function_from_operation_id(self, operation_id):
        module, controller_name, operation = operation_id.rsplit('.', 2)
        controller_module = importlib.import_module(module)
        controller_cls = getattr(controller_module, controller_name)
        controller = controller_cls(app=self.app)
        return getattr(controller, operation)


def connexion_blueprint(app, swagger_file):
    con = connexion.FlaskApp('hero_api', app.instance_path)
    api_con = con.add_api(swagger_file, resolver=Heroes(app=app))
    bp = Blueprint('heroes_swagger_ui', __name__)
    bp.add_url_rule('/api/heroes/ui/',
                    view_func=lambda: Environment(loader=FileSystemLoader(swagger_ui_3_path),
                                                  trim_blocks=True).get_template('index.j2').render(
                        openapi_spec_url="/api/heroes/openapi.json"
                    ), methods=['GET'])
    app.register_blueprint(bp)
    app.register_blueprint(api_con.blueprint)
    return api_con


def init(app: Flask):
    connexion_blueprint(app, 'swagger/main.yaml')
