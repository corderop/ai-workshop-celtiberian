from fastapi import FastAPI

from .phrases.repository import PhrasesRepository

app = FastAPI()


@app.get("/")
def root():
    repository = PhrasesRepository()
    return repository.get_all()


@app.get("/authors")
def authors():
    repository = PhrasesRepository()
    return repository.get_all_authors()
