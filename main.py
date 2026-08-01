from typing import Optional

from fastapi import Body, FastAPI, HTTPException, Response, status
from pydantic import BaseModel


class Post(BaseModel):
    title:str
    content:str
    isPublished: Optional[bool]=False


my_posts= [
    {
        "title": "Learning FastAPI",
        "content": "FastAPI is a modern Python web framework.",
        "isPublished": True
    },
    {
        "title": "Python Basics",
        "content": "Variables, loops, and functions are fundamental concepts.",
        "isPublished": True
    },
    {
        "title": "REST APIs",
        "content": "REST APIs use HTTP methods like GET, POST, PUT, and DELETE.",
        "isPublished": False
    },
    {
        "title": "Pydantic Models",
        "content": "Pydantic validates request and response data.",
        "isPublished": True
    },
    {
        "title": "Async Programming",
        "content": "Async functions improve performance for I/O-bound tasks.",
        "isPublished": False
    }
]

app=FastAPI()

@app.get("/")
def root():
    return {"message":"hello fastapi"}



@app.get("/posts")
def get_posts():
    return {"data":my_posts};

@app.get("/posts/{id}")
def get_posts_id(id:int,response:Response):
    post=my_posts[id] if id<len(my_posts) else None
    # if post==None:
    #     response.status_code=status.HTTP_404_NOT_FOUND
    # this is one way, but we will use the HTTPExcetipon

    if post==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"No post found with the id: {id}")
    return {"data":post}

@app.post("/posts",status_code=status.HTTP_201_CREATED) 
# status_code sets the default status_code
def create_posts(payload:Post):
    my_posts.append(payload.model_dump());
    print(payload)
    print(payload.model_dump())
    return {"data":my_posts}


