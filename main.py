from fastapi import FastAPI
from model import ScoreModel
import controller

app = FastAPI()

ScoreModel.init_table()

app.include_router(controller.router)

@app.get("/")
def read_root():
    return {
        "message": "서버 정상 가동 중",
        "version": "1.2"
    }
