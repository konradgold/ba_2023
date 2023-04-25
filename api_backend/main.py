from __future__ import annotations

from typing import List

from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from starlette import status

from api_backend.search import plainSearch
from elasticsearch import Elasticsearch
from pydantic import BaseModel

es_host = "http://localhost:9200"
es_user = "elastic"
es_password = "1234"

class Incoming(BaseModel):
    searchstring: str

    class Config:
        orm_mode = True

class Item(BaseModel):
    result: dict

    class Config:
        orm_mode = True


class JS(Item):
    response: list[Item]


app = FastAPI()
es = Elasticsearch(
    hosts=es_host,  # "http://localhost:9200"
    basic_auth=(es_user, es_password)
)
origins = [
    "http://localhost:4000",
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/search",
    summary="get search results",
    status_code=status.HTTP_200_OK,
    response_model=Item)
def search(item: Incoming):
    print(item.searchstring)
    return Item(result=plainSearch(item.searchstring, es))

@app.options("/search",
    summary="get search results",
    status_code=status.HTTP_200_OK,
    response_model=JS)
def search(item: JS):
    print(item)
    return JS(content=plainSearch(item.searchstring, es))
