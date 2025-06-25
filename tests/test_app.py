from http import HTTPStatus


def test_root_deve_retornar_ola_mundo(client):
    response = client.get('/')

    assert response.json() == {'message': 'Olá Mundo'}
    assert response.status_code == HTTPStatus.OK


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'Robert',
            'email': 'robert@example.com',
            'password': 'senhabolada',
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'id': 1,
        'email': 'robert@example.com',
        'username': 'Robert',
    }
