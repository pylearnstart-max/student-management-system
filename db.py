
import os
import psycopg2
from dotenv import load_dotenv


# Load .env file for local development
load_dotenv()


def get_connection():
    """
    Create and return a PostgreSQL database connection.
    Values are read from environment variables.
    """

    host = os.getenv("DB_HOST")
    port = os.getenv("DB_PORT", "5432")
    database = os.getenv("DB_NAME")
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")

    # Check required environment variables
    required = {
        "DB_HOST": host,
        "DB_PORT": port,
        "DB_NAME": database,
        "DB_USER": user,
        "DB_PASSWORD": password
    }

    missing = [
        key for key, value in required.items()
        if not value
    ]

    if missing:
        raise ValueError(
            f"Missing database environment variables: {', '.join(missing)}"
        )

    return psycopg2.connect(
        host=host,
        port=int(port),
        dbname=database,
        user=user,
        password=password
    )


# Test database connection locally
if __name__ == "__main__":
    try:
        conn = get_connection()
        print("Database Connected Successfully")
        conn.close()

    except Exception as e:
        print("Database Connection Failed:", e)
