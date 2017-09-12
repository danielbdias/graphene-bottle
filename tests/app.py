from bottle import Bottle
from graphene_bottle import graphql_middleware
from .schema import root_schema


def create_app(path='/graphql'):
    app = Bottle(debug=True)
    return app


if __name__ == '__main__':
    app = create_app(graphiql=True)
    app.run()
