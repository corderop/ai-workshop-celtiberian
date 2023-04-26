from typing import Annotated, Union

import openai
from fastapi import FastAPI, Query

from .config import API_KEY

app = FastAPI()

openai.api_key = API_KEY


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

    prompt_image = (
        f"Engineering course cover with the phrase {phrase} technology and service "
        f"made with an image that represents these key points: {', '.join(key_points)}"
    )
    response = openai.Image.create(
        prompt=prompt_image,
        n=1,
        size="512x512",
    )

    message = completion.choices[0].message.content
    image_url = response["data"][0]["url"]

    json_reponse = {"message": message, "image_url": image_url}

    return json_reponse
