from database import get_db_connection

class ScoreModel:
    @staticmethod
    def init_table():
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS rankings (
                id INTEGER PRIMARY KEY AUTOINCREAMENT,
                name TEXT NOT NULL,
                score INTEGER NOT NULL,
                date TIMESTAMP DEFAULT CURRENT TIMESTAMP
            )
        ''')
        conn.commit()
        conn.close()