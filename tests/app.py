from bottle import Bottle
from webtest import TestApp
import graphene

from graphene_bottle import graphql_middleware

class SystemQueries(graphene.ObjectType):
  hello = graphene.String(name=graphene.String(default_value="stranger"))

  def resolve_hello(self, info, name):
    return 'Hello ' + name

schema = graphene.Schema(query=SystemQueries)

def create_app(path='/graphql', test_mode=False):
    app = Bottle()
    graphql_middleware(app, path, schema)

    if test_mode:
        return TestApp(app)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)
