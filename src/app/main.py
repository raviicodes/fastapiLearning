from time import time
from typing import Optional

from fastapi import Body, FastAPI, HTTPException, Response, status
import psycopg
from pydantic import BaseModel


class Post(BaseModel):
    title:str
    content:str
    isPublished: Optional[bool]=False

app=FastAPI()


while True:
    try:
        connection= psycopg.connect(
        host='localhost',
        dbname='fastapi',
        user='postgres',
        password='PostgreSQL',
        port=5432

         ) ;
        cursor=connection.cursor();
        print("connection succesful")
        print("connection:",connection);
        print("cursor:",cursor)  
        break    

    except Exception as error:
        print("Failed to connect")
        print("Error is: ",error)
        time.sleep(2)



@app.get("/")
def root():
    return {"message":"hello fastapi"}



@app.get("/posts")
def get_posts():
    methodCall=cursor.execute("SELECT * FROM posts")
    posts=methodCall.fetchall()
    return {"data":posts}
