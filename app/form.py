from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.post('/login/')
async def login(username: str = Form(...), password: str = Form(...)):
    if password == "123":
        return {"username": username, "logado":True}
    return {"username": username, "logado":False}


@app.get('/')
async def main():
    content = """
        <form action="/login/" enctype="multipart/form-data" method="post">
        <input name="username" type="text" multiple>
        <input name="password" type="password" multiple>
        <input type="submit">
    """
    return HTMLResponse(content=content)
