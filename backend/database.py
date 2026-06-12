import sqlite3

def create_database():

    conn = sqlite3.connect("../database/predictions.db")

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS predictions(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        age REAL,
        nscore REAL,
        escore REAL,
        oscore REAL,
        ascore REAL,
        cscore REAL,
        impulsive REAL,
        ss REAL,
        prediction INTEGER,
        probability REAL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()

create_database()
def save_prediction(
    age,
    nscore,
    escore,
    oscore,
    ascore,
    cscore,
    impulsive,
    ss,
    prediction,
    probability
):

    conn = sqlite3.connect("../database/predictions.db")

    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO predictions(
        age,
        nscore,
        escore,
        oscore,
        ascore,
        cscore,
        impulsive,
        ss,
        prediction,
        probability
    )
    VALUES (?,?,?,?,?,?,?,?,?,?)
    """,
    (
        age,
        nscore,
        escore,
        oscore,
        ascore,
        cscore,
        impulsive,
        ss,
        prediction,
        probability
    ))

    conn.commit()
    conn.close()