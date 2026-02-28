from fastapi import FastAPI
import logging


logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

app = FastAPI()
logger = logging.getLogger(__name__)

@app.get("/")
def read_root():
    logger.info('Handled GET / request')
    
    return {
        "Hello": "World",
        "Branch": "development",
    }


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    logger.info(f'Handled GET /items/{item_id} request')
    
    return {"item_id": item_id, "q": q}
