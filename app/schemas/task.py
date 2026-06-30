from pydantic import BaseModel, ConfigDict
from typing import Optional

class TaskCreate(BaseModel):
    title: str
    description: str | None = None

class TaskResponse(BaseModel):
    id: int
    title: str
    description: str | None = None
    owner_id: int
    completed: bool

    model_config = ConfigDict(

        from_attributes = True

    )

class TaskUpdate(BaseModel):
    title: Optional[str] = None 
    description: Optional[str] = None
    completed: Optional[bool] = None