from flask import Flask
import psycopg2
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

try:
    conn = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )
    print("Database connection successful!")
except Exception as e:
    print(f"Database connection failed: {e}")

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, OpenShift!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
