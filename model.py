from database import get_db_connection

class ScoreModel:
    @staticmethod
    def init_table():
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS rankings (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    score INTEGER NOT NULL,
                    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            conn.commit()
        except Exception as e:
            print(f"테이블 생성 오류: {e}")
        finally:
            if conn:
                conn.close()
        
    @staticmethod
    def add_score(name: str, score: int):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            
            cursor.execute('''
                    INSERT INTO rankings (name, score) VALUES (?, ?)
            ''', (name, score))
            
            print("데이터 커밋 직전")
            conn.commit()
        except Exception as e:
            print(f"점수 추가 오류: {e}")
        finally:
            if conn:
                conn.close()
        
    @staticmethod
    def get_top_scores():
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            
            cursor.execute('''
                    SELECT name, score, date FROM rankings ORDER BY score DESC LIMIT 10''')
            rows = cursor.fetchall()
        except Exception as e:
            print(f"점수 조회 오류: {e}")
            rows = []
        finally:
            if conn:
                conn.close()
        return [dict(row) for row in rows]