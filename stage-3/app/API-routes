from fastapi import FastAPI
from .async_tasks import handle_stock_event
from .cache import get_cached_inventory

app = FastAPI()

@app.get("/inventory/{store_id}")
async def get_inventory(store_id: int):
   
    return get_cached_inventory(store_id)

@app.post("/stock/event")
async def post_stock_event(event: dict):
    # Async processing with message queue
    handle_stock_event(event)
    return {"status": "processing"}
