from fastapi import FastAPI


app = FastAPI()


@app.get('/file/read/{filename}', status_code=200)
async def read_file(filename: str):
    try:
        file = open(filename, 'r')
        return {'message': file.read()}
    except FileNotFoundError:
        return {'message': 'File not found'}

@app.get('/file/write/{filename}/{content}', status_code=200)
async def write_file(filename: str, content: str):
    try:
        file = open(filename, 'a')
        file.write(content+"\n")
        file.close()
        return {'message': 'gravado com sucesso'}
    except FileNotFoundError:
        return {'message': 'File not found'}
