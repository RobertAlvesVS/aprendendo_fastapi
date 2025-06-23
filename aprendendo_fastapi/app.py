from http import HTTPStatus
from aprendendo_fastapi.schemas import Message
from fastapi import FastAPI

app = FastAPI(title='Aprendendo API')


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olá Mundo'}
