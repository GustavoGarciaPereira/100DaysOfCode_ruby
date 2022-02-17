from typing import Optional
from fastapi import FastAPI, Query

app = FastAPI()


@app.get('/items/')
async def read_items(
            q: Optional[str] = Query(
                "padão",
                min_length=3,
                max_length=30)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"item_id": q})
    return results
