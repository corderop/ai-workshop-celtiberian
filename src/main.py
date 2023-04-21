from fastapi import FastAPI

from .phrases.repository import PhrasesRepository

app = FastAPI()


@app.get("/")
def root():
    repository = PhrasesRepository()
    return repository.get_all()


@app.get("/authors/phrases")
def author_phrases(author_name: str, readable: bool = False):
    repository = PhrasesRepository()
    return repository.get_author_phrases(author_name)


@app.get("/authors")
def authors():
    repository = PhrasesRepository()
    return repository.get_all_authors()
