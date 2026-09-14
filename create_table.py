from db import get_connection


def create_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            student_id SERIAL PRIMARY KEY,
            student_name VARCHAR(100) NOT NULL,
            email VARCHAR(100) UNIQUE NOT NULL,
            phone VARCHAR(15),
            course VARCHAR(100),
            age INTEGER,
            status VARCHAR(20) DEFAULT 'Active'
        )
    """)

    conn.commit()
    cursor.close()
    conn.close()

    print("Students Table Created Successfully")


if __name__ == "__main__":
    create_table()