
from fastapi import FastAPI
from easycharts import ChartServer

app = FastAPI()


@app.on_event('startup')
async def setup():
    app.charts = await ChartServer.create(
        app,
        charts_db="test"
    )
    await app.charts.create_dataset(
        "test",
        labels=['a', 'b', 'c'],
        dataset=[1, 2, 3, 4]
    )
