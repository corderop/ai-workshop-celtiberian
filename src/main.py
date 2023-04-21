from fastapi import FastAPI

from .phrases.repository import PhrasesRepository
from .phrases.service import PhrasesService

app = FastAPI()


@app.get("/")
def root():
    service = PhrasesService()
    return "\n".join(service.get_readable_sentences())


@app.get("/authors")
def authors():
    repository = PhrasesRepository()
    return repository.get_all_authors()
