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
        
        @staticmethod
        def add_score(name: str, score: int):
            conn = get_db_connection()
            cursor = conn.cursor()
            
            cursor.execute('''
                    INSERT INTO rankings (name, score) VALUES (?, ?)
            ''', (name, score))
            
            conn.commit()
            conn.close()
            
        @staticmethod
        def get_top_scores():
            conn = get_db_connection()
            cursor = conn.cursor()
            
            cursor.execute('''
                    SELECT name, score, date FROM rankings ORDER BY score DESC LIMIT 10''')
            rows = cursor.fetchall()
            conn.close()
            return rows