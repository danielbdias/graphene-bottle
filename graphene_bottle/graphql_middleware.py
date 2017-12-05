import json
from collections import namedtuple

from bottle import request, response

def handle_graphql_response(func, graphene_schema):
    def wrapper():
        response.content_type = 'application/json'

        try:
            result = func(graphene_schema)
            output = {'data': result.data}

            if result.errors is not None:
                output['errors'] = result.errors

            return json.dumps(output)
        except Exception as e:
            return json.dumps({'data': None, 'errors': [e]})

    return wrapper

def execute_get(graphene_schema):
    graphql_query = request.query['query']

    return graphene_schema.execute(graphql_query)

def execute_post(graphene_schema):
    graphql_data = request.json
    graphql_query = graphql_data['query']

    return graphene_schema.execute(graphql_query)

def execute_introspection(graphene_schema):
    DataItem = namedtuple('DataItem', ['data', 'errors'])
    return DataItem(data=graphene_schema.introspect(), errors=None)

def graphql_middleware(bottle_app, endpoint_name, graphene_schema):
    bottle_app.route(endpoint_name, 'OPTIONS',
                     handle_graphql_response(execute_introspection, graphene_schema))
    bottle_app.route(endpoint_name, 'POST',
                     handle_graphql_response(execute_post, graphene_schema))
    bottle_app.route(endpoint_name, 'GET',
                     handle_graphql_response(execute_get, graphene_schema))
