from fastapi import FastAPI

from app.database import engine, Base

import app.models

from app.routers import auth, tasks

from app.handlers.exception_handlers import(
    task_not_found_handler
)

from app.exceptions.task_exceptions import(
    TaskNotFoundException
)

from app.exceptions.user_exceptions import (
    
    UserNotFoundException,
    InvalidCredentialsException,
    UsernameAlreadyExistsException,
    EmailAlreadyExistsException
)

from app.handlers.exception_handlers import (
    
    user_not_found_handler,
    invalid_credentials_handler,
    username_already_exists_handler,
    email_already_exists_handler
)


app = FastAPI()

app.add_exception_handler(

    TaskNotFoundException,
    task_not_found_handler
)
    
app.add_exception_handler(
    
    UserNotFoundException,
    user_not_found_handler
)

app.add_exception_handler(

    InvalidCredentialsException,
    invalid_credentials_handler
)

app.add_exception_handler(

    UsernameAlreadyExistsException,
    username_already_exists_handler
)

app.add_exception_handler(
    EmailAlreadyExistsException,
    email_already_exists_handler
)   


app.include_router(auth.router)
app.include_router(tasks.router)


@app.get("/")
def home():
    return {"message": "Project clean and working"}

