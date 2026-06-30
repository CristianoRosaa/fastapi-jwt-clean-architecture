from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.database import get_db

from app.models import task as models
from app.models import user as user_models

from app.schemas import task as schemas

from app.core.dependencies import get_current_user

from typing import List, Optional

from app.services.task_service import (
    get_user_tasks,
    create_task
)

from app.services import task_service



router = APIRouter()


@router.post(
    "/tasks",
    response_model=schemas.TaskResponse
)

def create_task_route(

    task: schemas.TaskCreate,

    current_user: user_models.User = Depends(
        get_current_user
    ),

    db: Session = Depends(get_db)
):

    return create_task(
        db = db,
        task = task,
        user = current_user
    )



@router.get(
    "/tasks",
    response_model=List[schemas.TaskResponse]
)

def get_tasks(

    skip: int = Query(

        default = 0,

        ge = 0,

        description = "Number of records to ignore"

    ),

    limit: int = Query(

        default = 10,

        ge = 1,

        le = 100,

        description = "Maximum number of tasks returned"

    ),

    completed: Optional[bool] = Query(
        default = None,
        description = "Filter completed tasks"
    ),

    title: str | None = Query(

        default = None,

        decription = "Search for tasks by title"

    ),

    order_by: str = Query(

        default = "id",

        description = "Order by: id, title completed"

    ),

    order: str = Query(

        default = "asc",

        description = "asc or desc"

    ),

    current_user: user_models.User = Depends(get_current_user),

    db: Session = Depends(get_db)

):

    return task_service.get_tasks(

        db = db,

        user = current_user,

        skip = skip,

        limit = limit,

        completed = completed,

        title = title,

        order_by = order_by,

        order = order

    )


@router.get(
    "/tasks/{task_id}",
    response_model=schemas.TaskResponse
)

def get_task(
    
    task_id: int,

    current_user: user_models.User = Depends(
        get_current_user
    
    ),

    db: Session = Depends(get_db)
):
    
    return task_service.get_task_by_id(

        db = db,

        task_id = task_id,

        user = current_user

    )


@router.put(
    "/tasks/{task_id}",
    response_model=schemas.TaskResponse
)

def update_task(

    task_id: int,

    task: schemas.TaskUpdate,
  
    current_user: user_models.User = Depends(
        get_current_user
    ),

    db: Session = Depends(get_db)

):
    
    return task_service.update_task(
        db=db,
        task_id=task_id,
        task_data=task,
        user=current_user
    )

@router.delete("/tasks/{task_id}")

def delete_task(

    task_id: int,

    current_user: user_models.User = Depends(

        get_current_user

    ),

    db: Session = Depends(get_db)

):
    return task_service.delete_task(
        db=db,
        task_id=task_id,
        user=current_user
    )

