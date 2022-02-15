
from fastapi import FastAPI

app = FastAPI()


@app.get('/algo/{item}')
async def main(item):
    return {"nome": item}


@app.get('/+/{i}/{o}')
async def mais(i: int, o: int):
    return {"nome": i+o}


@app.get('/-/{i}/{o}')
async def manos(i: int, o: int):
    return {"nome": i-o}


@app.get('/*/{i}/{o}')
async def vezes(i: int, o: int):
    return {"nome": i*o}
