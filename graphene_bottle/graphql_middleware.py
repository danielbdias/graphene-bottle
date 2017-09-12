import json
from collections import namedtuple

from bottle import request, response


def json_response(data):
    response.content_type = 'application/json'
    return json.dumps(data)


def handle_graphql_response(func, graphene_schema):
    def wrapper(func, graphene_schema):
        try:
            result = func()
            output = {'data': result.data}

            if result.errors is not None:
                output['errors'] = result.errors

            return json_response(output)
        except Exception as e:
            return json_response({'data': None, 'errors': [e]})

    return wrapper


def execute_post(graphene_schema):
    graphql_data = request.json
    graphql_query = graphql_data['query']

    return graphene_schema.execute(graphql_query)


def execute_introspection(graphene_schema):
    DataItem = namedtuple('DataItem', ['data', 'errors'])
    return DataItem(data=graphene_schema.introspect(), errors=None)


def execute_post_query(graphene_schema):
    return handle_graphql_response(execute_post, graphene_schema)


def execute_introspection_query(graphene_schema):
    return handle_graphql_response(execute_introspection, graphene_schema)


def graphql_middleware(bottle_app, endpoint_name, graphene_schema):
    bottle_app.route(endpoint_name, 'OPTIONS',
                     execute_introspection_query(graphene_schema))
    bottle_app.route(endpoint_name, 'POST',
                     execute_post_query(graphene_schema))
