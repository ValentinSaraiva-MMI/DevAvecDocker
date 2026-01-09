import psycopg2
import os
import redis
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

# Connexion Redis
r = redis.Redis(host=os.getenv("REDIS_HOST", "redis"), port=6379, decode_responses=True)

def get_db_connection():
    return psycopg2.connect(
        host=os.getenv("POSTGRES_HOST"),
        port=5432,
        user=os.getenv("POSTGRES_USER", "postgres"),
        password=os.getenv("POSTGRES_PASSWORD"),
        database=os.getenv("POSTGRES_DB", "mydb")
    )

@app.get("/")
async def get_dashboard_data():
    results = []
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute("SELECT id, nom, prenom, email, promo FROM students")
        rows = cursor.fetchall()
        colnames = [desc[0] for desc in cursor.description]
        
        for row in rows:
            student = dict(zip(colnames, row))    
            student_id = student['id']
            redis_key = f"student:{student_id}:views"
            
            try:
                views = r.incr(redis_key)
                student['views'] = views
            except redis.ConnectionError:
                student['views'] = "N/A (Cache HS)"

            results.append(student)

        cursor.close()
        conn.close()
        
    except Exception as e:
        print(f"Erreur API: {e}")
        return [{"nom": "Erreur", "promo": str(e)}]

    return results