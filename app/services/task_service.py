from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.models.task import Task
from app.models.user import User

from app.schemas.task import(
    TaskCreate,
    TaskUpdate
)

from app.repositories import task_repository

from app.exceptions.task_exceptions import TaskNotFoundException

from app.core.logger import logger

def get_user_tasks(
        db: Session,
        user_id: int
):
    
    tasks = db.query(Task).filter(
        Task.owner_id == user_id
    ).all()

    return tasks


def create_task(
    
    db: Session,

    task: TaskCreate,

    user: User

):
    
    logger.info(

        f"User {user.username} creating task"
    
    )

    new_task = Task(

        title = task.title,

        description = task.description,

        owner_id = user.id,

        completed = False

    )    

    logger.info(
        
        f"Task created successfully"
    
    )

    return task_repository.create(
        
        db,

        new_task

    )



def get_tasks(
        
        db: Session,

        user: User,

        skip: int = 0,

        limit: int = 10,

        completed: bool | None = None,

        title: str | None = None,

        order_by: str = "id",

        order: str = "asc"

):
    
    logger.info(

        f"Listing tasks from user {user.username}"

    )

    return task_repository.get_all_by_user(

        db,
        
        user.id,

        skip,

        limit, 

        completed,

        title,

        order_by,

        order 

    )   


def get_task_by_id(
        
        db: Session,

        task_id: int,

        user: User
):
    
    logger.info(

        f"User {user.username} requesting task {task_id}"

    )

    task = task_repository.get_by_id(
        db,

        task_id,

        user.id
    )

    if task is None:
        
        logger.info(

            f"Task {task_id} not found"

        )
        
        raise TaskNotFoundException()
    
    return task


def update_task(
        
        db: Session,

        task_id: int,

        task_data: TaskUpdate,
        
        user: User
):
    
    logger.info(

        f"Updating task {task_id}"
    )

    task = task_repository.get_by_id(
        
        db,
        
        task_id,

        user.id
    )

    if task is None:
        
        logger.warning(

            f"Task {task_id} not found"

        )

        raise TaskNotFoundException()
    
    if task_data.title is not None:
        task.title = task_data.title

    if task_data.description is not None:
        task.description = task_data.description

    if task_data.completed is not None:
        task.completed = task_data.completed


    return task_repository.update(

        db,

        task
    )


def delete_task(
        
        db: Session,
        
        task_id: int,
        
        user: User
):

    logger.info(

        f"Deleting task {task_id}"

    )

    task = task_repository.get_by_id(

        db,

        task_id,

        user.id

    )

    if task is None:
        
        logger.warning(

            f"Task {task_id} not found"

        )

        raise TaskNotFoundException()
    
    task_repository.delete(

        db,

        task
    )


    return{
        
        "message": "Task deleted successfully"
    }
