from time import time
from typing import Optional
from fastapi import Body, FastAPI
from pydantic import BaseModel
from sqlalchemy import text
from app.db.database import engine

class Post(BaseModel):
    title:str
    content:str
    isPublished: Optional[bool]=False

app=FastAPI()


while True:
    try:
        connection=engine.connect()
        print("Database connection was successful")
        break
    except Exception as error:
        print("Database connection failed")
        print("Error:",error)
        time.sleep(2)
    



@app.get("/")
def root():
    return {"message":"hello fastapi"}



@app.get("/posts")
def get_posts():
    results=connection.execute(text("SELECT * FROM posts"))
    posts=results.mappings().all()
    return {"data":posts}
