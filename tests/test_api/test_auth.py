def test_register_and_login(client):
    register_data = {
        "email": "test@example.com",
        "password": "password123",
        "first_name": "Test",
        "last_name": "User",
        "favorite_genre_id": None
    }

    r = client.post("/auth/register", json=register_data)
    assert r.status_code == 200
    assert "access_token" in r.json()

    login_data = {
        "email": "test@example.com",
        "password": "password123"
    }

    r = client.post("/auth/login", params=login_data)
    assert r.status_code == 200
    assert "access_token" in r.json()
