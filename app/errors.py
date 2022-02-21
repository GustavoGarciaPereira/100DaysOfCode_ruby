from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse


class UnicornException(Exception):
    def __init__(self, name: str):
        self.name = name


app = FastAPI()


@app.exception_handler(UnicornException)
async def uniconrn_exeception_handler(request: Request, exc: UnicornException):
    return JSONResponse(
        status_code=418,
        content={"massage": f'Opps! {exc.name}'}
    )


@app.get('/request/{name}')
async def main(name: str):
    if name == "gustavo":
        raise UnicornException(name=name)
    return {"main": name}
