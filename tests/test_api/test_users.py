def test_get_me(client):
    register_data = {
        "email": "me@example.com",
        "password": "password123",
        "first_name": "Me",
        "last_name": "User",
        "favorite_genre_id": None
    }

    r = client.post("/auth/register", json=register_data)
    token = r.json()["access_token"]

    headers = {"Authorization": f"Bearer {token}"}
    r = client.get("/users/me", headers=headers)

    assert r.status_code == 200
    assert r.json()["email"] == "me@example.com"
