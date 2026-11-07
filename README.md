# 📦 Gestion d'items : FastAPI + Streamlit

Petite application web pour créer et consulter des items (nom, prix, stock). Le projet est composé de deux parties : une **API REST** (FastAPI) et une **interface utilisateur** (Streamlit) qui communique avec l'API.

## 🌐 Démo en ligne

- **Interface** : [URL de ton app Streamlit]
- **API** : [URL de ton API Render]
- **Documentation interactive de l'API** : [URL de ton API Render]/docs

> ⚠️ L'API est hébergée sur l'offre gratuite de Render : elle se met en veille après 15 minutes d'inactivité. La première requête peut donc prendre environ une minute. Les données sont stockées en mémoire et sont réinitialisées à chaque redémarrage.

## 🏗️ Architecture

```
┌──────────────┐   requêtes HTTP   ┌──────────────┐
│  Streamlit   │ ────────────────► │   FastAPI    │
│  (frontend)  │ ◄──────────────── │  (backend)   │
└──────────────┘      JSON         └──────────────┘
   app.py                             main.py
```

- **FastAPI** expose les routes, valide les données avec Pydantic et stocke les items en mémoire.
- **Streamlit** fournit le formulaire d'ajout et le tableau des items, en appelant l'API avec `requests`.

## 🛠️ Technologies

- [FastAPI](https://fastapi.tiangolo.com/) : API REST
- [Pydantic](https://docs.pydantic.dev/) : validation des données
- [Streamlit](https://streamlit.io/) : interface utilisateur
- [pytest](https://docs.pytest.org/) : tests
- [Ruff](https://docs.astral.sh/ruff/) : lint
- GitHub Actions : intégration continue
- Render et Streamlit Community Cloud : déploiement

## 📁 Structure du projet

```
fastapi/
├── .github/workflows/ci.yml   # pipeline d'intégration continue
├── main.py                    # API FastAPI
├── app.py                     # interface Streamlit
├── test_main.py               # tests de l'API
├── requirements.txt           # dépendances Python
└── .gitignore
```

## 🔌 Routes de l'API

| Méthode | Route | Description |
|---|---|---|
| `GET` | `/` | Message de bienvenue |
| `POST` | `/items` | Crée un item |
| `GET` | `/items` | Liste tous les items |
| `GET` | `/items/{item_id}` | Lit un item par son identifiant (404 si introuvable) |

Exemple de corps pour `POST /items` :

```json
{
  "nom": "Clavier",
  "prix": 49.99,
  "en_stock": true
}
```

## 🚀 Lancer le projet en local

### 1. Cloner et installer

```bash
git clone https://github.com/Joseph-Willson/fastapi.git
cd fastapi

python -m venv .env
.env\Scripts\activate        # Windows
# source .env/bin/activate   # macOS / Linux

pip install -r requirements.txt
```

### 2. Lancer l'API (terminal 1)

```bash
fastapi dev main.py
```

L'API est disponible sur http://127.0.0.1:8000 et sa documentation sur http://127.0.0.1:8000/docs.

### 3. Lancer l'interface (terminal 2)

```bash
streamlit run app.py
```

L'interface s'ouvre sur http://localhost:8501.

### Configuration

L'interface lit l'adresse de l'API dans la variable d'environnement `API_URL`. Sans valeur, elle utilise `http://127.0.0.1:8000`.

```bash
# Windows (PowerShell)
$env:API_URL="https://mon-api.onrender.com"

# macOS / Linux
export API_URL="https://mon-api.onrender.com"
```

## ✅ Tests et qualité du code

```bash
pytest              # lance les tests
ruff check .        # vérifie le style et les imports
ruff check . --fix  # corrige automatiquement
```

## 🔄 CI/CD

- **CI** : à chaque push et pull request, GitHub Actions installe les dépendances, lance `ruff` puis `pytest` (voir `.github/workflows/ci.yml`).
- **CD** : Render redéploie l'API et Streamlit Community Cloud redéploie l'interface à chaque push sur la branche `main`.

## 🗺️ Pistes d'amélioration

- [ ] Persistance des données avec une base (SQLite, PostgreSQL)
- [ ] Suppression et modification des items (`DELETE`, `PUT`)
- [ ] Authentification (OAuth2 / JWT)
- [ ] Conteneurisation avec Docker
- [ ] Organisation du code avec `APIRouter`

## 👤 Auteur

Joseph Willson, [@Joseph-Willson](https://github.com/Joseph-Willson)
