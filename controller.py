from fastapi import APIRouter
from model import ScoreModel
from schema import ScoreInput, RangkingOutput
from typing import List

router = APIRouter(prefix="/api") 

@router.post("/submit")
def submit_score(data: ScoreInput):
    print(f"받은 데이터 : {data}")
    ScoreModel.add_score(data.name, data.score)
    return {"message" : "점수 저장 완료"}

@router.get("/rankings", response_model=List[RangkingOutput])
def get_rankings():
    rankings = ScoreModel.get_top_scores()
    return rankings