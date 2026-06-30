from sqlalchemy.orm import Session

from app.models.task import Task

def get_all_by_user(
        
    db: Session,

    user_id: int,

    skip: int = 0,

    limit: int = 10,

    completed: bool | None = None,

    title: str | None = None,

    order_by: str = "id",

    order: str = "asc"

):

    query = db.query(Task).filter(

        Task.owner_id == user_id

    )

    if completed is not None:
        query = query.filter(

            Task.completed == completed

        )
    
    if title: 

        query = query.filter(

            Task.title.ilike(f"%{title}%")

        )

    allowed_columns = {

        "id": Task.id,

        "title": Task.title,

        "completed": Task.completed 

    }

    column = allowed_columns.get(order_by, Task.id)

    if order.lower() == "desc":

        query = query.order_by(column.desc())   

    else:

        query = query.order_by(column.asc())


    return (

        query
        .offset(skip)
        .limit(limit)
        .all()

    )


def get_by_id(
        
        db: Session,

        task_id: int,

        user_id: int
):
    
    return db.query(Task).filter(

        Task.id == task_id,

        Task.owner_id == user_id

    ).first()

def create(
        db: Session,

        task: Task
):
    db.add(task)

    db.commit()

    db.refresh(task)

    return task

def delete(
        db: Session,

        task: Task
):
    
    db.delete(task)

    db.commit()


def update(
        db: Session,
        task: Task
):
    
    db.commit()

    db.refresh(task)

    return task 

