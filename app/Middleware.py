# create app with fastAPI and middleware 

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import time


app = FastAPI()

origins = [
    "http://gugu",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.middleware('http')
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers['X-Process-Time'] = str(process_time)
    response.headers['hello'] = "hey you made a request big friend"
    return response





@app.get('/')
async def root():
    return {'message': 'Hello World'}

@app.post('/')
async def root():
    return {'message': 'Hello World'}