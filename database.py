"""
Tietokanta-asetukset ja mallit Todo API:lle.
Käyttää SQLite-tietokantaa ja SQLAlchemy ORM:ää.
"""

from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLite-tietokannan sijainti (luodaan todos.db tiedosto)

DATABASE_URL = "sqlite:///./todos.db"

# Luo tietokanta-engine
# check_same_thread=False: Sallii usean säikeen käytön SQLitessä

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False}
)

# Session: Tietokantayhteyksien hallinta

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#base-luokka tietokanta mallille

Base = declarative_base()

#todo-malli

class Todo(Base):

    """
    Todo-malli tietokantaan.
    
    Attribuutit:
        id (int): Tehtävän yksilöllinen tunniste (primary key)
        task (str): Tehtävän kuvaus
        completed (bool): Onko tehtävä suoritettu (oletus: False)
    """
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True,index=True)
    task = Column(String, index=True)
    completed = Column(Boolean, index=False)

# Luo kaikki taulut tietokantaan

Base.metadata.create_all(bind=engine)
    