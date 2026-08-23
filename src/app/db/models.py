from sqlalchemy import Boolean, Column, Integer, MetaData, String, Table, create_engine, text
from .database import engine
metadata=MetaData()

posts=Table(
    "posts",
    metadata,
    Column("id",Integer,primary_key=True,index=True),
    Column("title",String(100)),
    Column("content",String(300)),
    Column("is_published",Boolean,nullable=False,default=False),
    Column("created_at",String,nullable=False,server_default=text("now()"))
)

metadata.create_all(engine)