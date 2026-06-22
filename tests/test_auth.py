from fastapi.testclient import TestClient
from application.main import app
client=TestClient(app)
def test_register():
    response=client.post("/auth/register",json={
        "email":"register@mail.com",
        "password":"qwerty123"
    })
    assert response.status_code==201
    assert response.json()["email"]=="register@mail.com"
def test_login_success():
    client.post("/auth/register",json={
        "email":"success@mail.com",
        "password":"qwerty123"
    })
    response=client.post("/auth/login",data={
        "username":"success@mail.com",
        "password":"qwerty123"
    })
    assert response.status_code==200
    assert "access_token" in response.json()
def test_register_duplicate_email():
    client.post("/auth/register",json={
        "email":"same@mail.com",
        "password":"qwerty123"
    })
    response=client.post("/auth/register",json={
        "email":"same@mail.com",
        "password":"qwerty123"
    })
    assert response.status_code==400
def test_login_wrong_password():
    client.post("/auth.register",json={
        "email":"wrong@mail.com",
        "password":"wrong123"
    })
    response=client.post("/auth/login",data={
        "username":"wrong@mail.com",
        "password":"wrong1234"
    })
    assert response.status_code==400