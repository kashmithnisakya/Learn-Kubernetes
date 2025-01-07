from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import psycopg2

app = FastAPI()

# Database connection
DB_CONFIG = {
    "dbname": "mydatabase",
    "user": "user",
    "password": "password",
    "host": "postgres-service",
    "port": 5432,
}

def connect_db():
    conn = psycopg2.connect(**DB_CONFIG)
    return conn

class CalculationRequest(BaseModel):
    a: int
    b: int

@app.post("/calculate")
def calculate(data: CalculationRequest):
    try:
        conn = connect_db()
        cursor = conn.cursor()
        # Example query: log the calculation to the database
        query = "INSERT INTO calculations (a, b, result) VALUES (%s, %s, %s)"
        result = data.a + data.b
        cursor.execute(query, (data.a, data.b, result))
        conn.commit()
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()
