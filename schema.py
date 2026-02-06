from pydantic import BaseModel

class ScoreInput(BaseModel):
    name : str
    score : int
    
class RangkingOutput(BaseModel):
    name : str
    score : int
    date : str
    