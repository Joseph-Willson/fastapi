from fastapi.testclient import TestClient
from main import app, items

client = TestClient(app)


def setup_function():
    items.clear()  # repartir d'une liste vide avant chaque test


def test_accueil():
    r = client.get("/")
    assert r.status_code == 200
    assert r.json() == {"message": "Bonjour FastAPI"}


def test_creer_et_lister_item():
    r = client.post("/items", json={"nom": "Clavier", "prix": 49.99})
    assert r.status_code == 200

    r = client.get("/items")
    assert len(r.json()) == 1
    assert r.json()[0]["nom"] == "Clavier"


def test_item_introuvable():
    r = client.get("/items/99")
    assert r.status_code == 404