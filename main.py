import os

from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

from config import UPLOAD_DIR
from routes import routes

app = FastAPI()

os.makedirs(UPLOAD_DIR, exist_ok=True)
app.mount("/uploads", StaticFiles(directory=UPLOAD_DIR), name="uploads")

for router in routes:
    app.include_router(router)
