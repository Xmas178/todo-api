"""
Todo API - Yksinkertainen tehtävälistan REST API
FastAPI + SQLite + SQLAlchemy

Endpoints:
- GET /tasks - Hae kaikki tehtävät
- POST /tasks - Lisää uusi tehtävä
- PUT /tasks/{id} - Päivitä tehtävän tila
- DELETE /tasks/{id} - Poista tehtävä
"""

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, Todo, engine, Base
from typing import Optional


# Luo taulut jos ei ole olemassa
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Todo API",
    description="Yksinkertainen REST API tehtävien hallintaan",
    version="1.0.0"
)


def get_db():
    """
    Dependency: Luo ja hallitsee tietokantayhteyden.

    Yields:
        Session: SQLAlchemy-sessio tietokantayhteydelle
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def read_root():
    """
    Juurireitti - tervetuloviesti.

    Returns:
        dict: Tervetuloviesti
    """
    return {"message": "Tervetuloa Todo API:iin!"}


@app.get("/tasks")
def get_tasks(db: Session = Depends(get_db)):
    """
    Hae kaikki tehtävät tietokannasta.

    Args:
        db: Tietokantayhteys (injektoidaan automaattisesti)

    Returns:
        list: Lista Todo-objekteja
    """
    tasks = db.query(Todo).all()
    return tasks


@app.post("/tasks")
def create_task(task: str, db: Session = Depends(get_db)):
    """
    Luo uusi tehtävä.

    Args:
        task: Tehtävän kuvaus
        db: Tietokantayhteys

    Returns:
        Todo: Luotu tehtävä-objekti ID:llä
    """
    new_task = Todo(task=task, completed=False)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task


@app.put("/tasks/{task_id}")
def update_task(task_id: int, completed: Optional[bool] = None, db: Session = Depends(get_db)):
    """
    Päivitä tehtävän tila.

    Args:
        task_id: Tehtävän ID
        completed: Uusi tila (True/False)
        db: Tietokantayhteys

    Returns:
        Todo: Päivitetty tehtävä tai virheviesti
    """
    task = db.query(Todo).filter(Todo.id == task_id).first()
    if not task:
        return {"error": "Tehtävää ei löytynyt"}

    if completed is not None:
        task.completed = completed

    db.commit()
    db.refresh(task)
    return task


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    """
    Poista tehtävä tietokannasta.

    Args:
        task_id: Poistettavan tehtävän ID
        db: Tietokantayhteys

    Returns:
        dict: Vahvistusviesti tai virheviesti
    """
    task = db.query(Todo).filter(Todo.id == task_id).first()
    if task:
        db.delete(task)
        db.commit()
        return {"message": "Tehtävä poistettu"}
    return {"error": "Tehtävää ei löytynyt"}
