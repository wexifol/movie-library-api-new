def test_get_movies(client):
    r = client.get("/movies")
    assert r.status_code == 200
    assert isinstance(r.json(), list)
