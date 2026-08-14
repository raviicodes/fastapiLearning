from sqlalchemy import create_engine

DB_URL="postgresql+psycopg://postgres:PostgreSQL@localhost:5432/fastapi"

engine=create_engine(DB_URL)

