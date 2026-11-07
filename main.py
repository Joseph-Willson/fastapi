from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    nom: str
    prix: float
    en_stock: bool = True


# Stockage en mémoire (perdu à chaque redémarrage)
items: list[Item] = []


@app.get("/")
def accueil():
    return {"message": "Bonjour FastAPI"}


@app.post("/items")
def creer_item(item: Item):
    items.append(item)
    return {"id": len(items) - 1, "item": item}


@app.get("/items")
def lister_items():
    return items


@app.get("/items/{item_id}")
def lire_item(item_id: int):
    if item_id < 0 or item_id >= len(items):
        raise HTTPException(status_code=404, detail="Item introuvable")
    return items[item_id]