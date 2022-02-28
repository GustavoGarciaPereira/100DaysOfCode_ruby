from fastapi import FastAPI
from routers import livros

app = FastAPI()


app.include_router(livros.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}
