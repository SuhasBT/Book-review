import pytest
from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_homepage(client):
    """Check homepage loads successfully"""
    response = client.get('/')
    assert response.status_code == 200
    assert b"Book Reviews" in response.data


def test_add_review(client):
    """Check adding a review works"""
    response = client.post(
        '/add',
        data={
            'title': 'The Hobbit',
            'text': 'A classic fantasy adventure.'
        },
        follow_redirects=True
    )
    assert response.status_code == 200
    assert b"The Hobbit" in response.data
    assert b"A classic fantasy adventure." in response.data


def test_reviews_api(client):
    """Check JSON API returns reviews"""
    client.post(
        '/add',
        data={'title': '1984', 'text': 'Dystopian masterpiece.'}
    )
    response = client.get('/reviews')
    assert response.status_code == 200
    data = response.get_json()
    assert any(r['title'] == '1984' for r in data['reviews'])
