# Todo API

Todella yksinkertainen REST API tehtävien hallintaan. Rakennettu FastAPI:lla ja SQLite-tietokannalla.

Ominaisuudet

- CRUD-operaatiot tehtäville (Create, Read, Update, Delete)
- SQLite-tietokanta pysyvään tallennukseen
- Automaattinen API-dokumentaatio (Swagger UI)
- Nopea ja moderni FastAPI-framework

Vaatimukset

- Python 3.8+
- pip (Python package manager)

Asennus

1. Kloonaa repositorio
```bash
git clone https://github.com/Xmas178/todo-api.git
cd todo-api
```

2. Luo virtuaaliympäristö
```bash
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate  # Windows
```

3. Asenna riippuvuudet
```bash
pip install fastapi uvicorn sqlalchemy
```

4. Käynnistä serveri
```bash
uvicorn main:app --reload
```

Serveri käynnistyy osoitteessa: `http://localhost:8000`

API-dokumentaatio

Automaattinen dokumentaatio
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

Endpointit

#### 1. Hae kaikki tehtävät
```http
GET /tasks
```

**Vastaus:**
```json
[
  {
    "id": 1,
    "task": "Opi FastAPI",
    "completed": false
  }
]
```

#### 2. Lisää uusi tehtävä
```http
POST /tasks?task=Uusi tehtävä
```

**Vastaus:**
```json
{
  "id": 2,
  "task": "Uusi tehtävä",
  "completed": false
}
```

#### 3. Päivitä tehtävän tila
```http
PUT /tasks/1?completed=true
```

**Vastaus:**
```json
{
  "id": 1,
  "task": "Opi FastAPI",
  "completed": true
}
```

#### 4. Poista tehtävä
```http
DELETE /tasks/1
```

**Vastaus:**
```json
{
  "message": "Tehtävä poistettu"
}
```

Projektin rakenne
```
todo-api/
├── main.py           # API-reititykset ja endpointit
├── database.py       # Tietokanta-asetukset ja mallit
├── todos.db          # SQLite-tietokanta (luodaan automaattisesti)
├── venv/             # Virtuaaliympäristö
└── README.md         # Tämä tiedosto
```

Testaus

Thunder Client (VS Code)
1. Asenna Thunder Client -laajennus
2. Luo uusi pyyntö
3. Testaa endpointit yllä olevien esimerkkien mukaan

cURL
```bash
# Hae tehtävät
curl http://localhost:8000/tasks

# Lisää tehtävä
curl -X POST "http://localhost:8000/tasks?task=Testitehtävä"

# Päivitä tehtävä
curl -X PUT "http://localhost:8000/tasks/1?completed=true"

# Poista tehtävä
curl -X DELETE "http://localhost:8000/tasks/1"
```

Teknologiat

- **FastAPI** - Moderni Python web framework
- **SQLAlchemy** - SQL-tieto)kanta ORM
- **SQLite** - Kevyt tietokanta
- **Uvicorn** - ASGI web server


Tässä projektissa käytin :
- REST API:n perusteet ja HTTP-metodit (GET, POST, PUT, DELETE)
- FastAPI-frameworkin käyttöä
- Tietokannan integroinnin SQLAlchemyn avulla
- API-dokumentoinnin ja testauksen

Jatkokehitysideoita

- [ ] Lisää käyttäjäautentikointi (JWT)
- [ ] Pydantic-mallit datan validointiin
- [ ] PostgreSQL-tuki tuotantokäyttöön
- [ ] Yksikkötestit (pytest)
- [ ] Docker-konttitus
- [ ] Frontend (React/Vue)


---

Tekijä: Sami Tommilammi  
Päivämäärä: 2.11.2025  
Projekti: Portfolio-projekti
