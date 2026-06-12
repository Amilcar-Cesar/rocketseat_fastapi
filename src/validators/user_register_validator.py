from pydantic import BaseModel, Field

class UserInput(BaseModel):
    username: str = Field(..., min_length=1)
    age: int = Field(..., gt=0)
    uf: str = Field(..., min_length=2, max_length=2)