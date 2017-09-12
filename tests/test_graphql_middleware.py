import pytest

def test_allows_get_with_query_param(client):
    response = client.get(url_string(query='{test}'))

    assert response.status_code == 200
    assert response_json(response) == {
        'data': {'test': "Hello World"}
    }
