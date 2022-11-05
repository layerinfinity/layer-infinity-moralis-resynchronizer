import os
from fastapi import FastAPI

app = FastAPI()

API_KEY = os.environ.get("MORALIS_KEY")
BASIC_AUTH_USER = os.environ.get("BASIC_AUTH_USER")
BASIC_AUTH_PASSWORD = os.environ.get("BASIC_AUTH_PASSWORD")
