from pydantic import BaseModel

class ScoreInput(BaseModel):
    name : str
    score : int
    
class ScoreOutput(BaseModel):
    name : str
    score : int
    date : str
    