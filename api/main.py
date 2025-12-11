import psycopg2
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

conn = psycopg2.connect(
        host=os.getenv("POSTGRES_HOST"),
        port=5432,
        user=os.getenv("POSTGRES_USER", "postgres"),
        password=os.getenv("POSTGRES_PASSWORD"),
        database=os.getenv("POSTGRES_DB", "mydb")
    )

@app.get("/users")
async def get_users():
    cursor = conn.cursor()
    sql_select_query = "SELECT * FROM users"
    cursor.execute(sql_select_query)
    records = cursor.fetchall()
    print("Nombre d'utilisateurs trouvés :", cursor.rowcount)
    cursor.close()
    return { "utilisateurs": records }