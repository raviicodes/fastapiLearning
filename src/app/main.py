from time import time
from typing import Optional
from fastapi import Body, FastAPI
from psycopg import connection
from pydantic import BaseModel
from sqlalchemy import insert, text
from app.db.database import engine
from app.db.models import posts

class Post(BaseModel):
    title:str
    content:str
    isPublished: Optional[bool]=False

app=FastAPI()

@app.get("/")
def root():
    return {"message":"hello fastapi"}



@app.get("/posts")
def get_posts():
    with engine.connect() as connection:
        results=connection.execute(text("SELECT * FROM posts"))
        posts=results.mappings().all()
        return {"data":posts}

@app.post("/posts")
def create_post(post: Post):
    with engine.begin() as connection:
        sql_statement=insert(posts);
        result=connection.execute(sql_statement, post.model_dump())
        return {"data":result.mappings().first()}