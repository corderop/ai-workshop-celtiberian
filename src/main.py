from typing import Annotated, Union

from fastapi import FastAPI, Query

import openai

from .config import API_KEY

app = FastAPI()

openai.api_key = API_KEY


@app.get("/")
def root():
    return API_KEY


@app.get("/summary")
def getSummary(
    phrase: str, key_points: Annotated[Union[list[str], None], Query()] = None
):
    prompt = (
        f"Genera un post LinkedIn de entre 200 y 500 palabras sobre un seminario titulado: {phrase}"
        f"con los siguientes puntos clave: {', '.join(key_points)}"
    )
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=[{"role": "user", "content": prompt}]
    )

    return completion.choices[0].message.content
