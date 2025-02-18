from fastapi import FastAPI
from src.config import settings
from src.http_client import CMCHTTPClient

from src.router import router as router_crypto
app=FastAPI()


app.include_router(router_crypto)


