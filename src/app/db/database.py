

from sqlalchemy import Boolean, Column, Integer, MetaData, String, Table, Table, create_engine, text
from app.config.config import DATABASE_URL

engine=create_engine(DATABASE_URL)

