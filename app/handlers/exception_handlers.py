from fastapi import Request 
from fastapi.responses import JSONResponse

from app.exceptions.task_exceptions import (
    TaskNotFoundException
)

from app.exceptions.user_exceptions import(
    UserNotFoundException,
    InvalidCredentialsException,
    UsernameAlreadyExistsException,
    EmailAlreadyExistsException
)

async def task_not_found_handler(
        
    request: Request,

    exc: TaskNotFoundException
):
    
    return JSONResponse(
        
        status_code=404,
        
        content={

            "detail": exc.message

        }
    )

async def user_not_found_handler(
    
    request: Request,
  
    exc: UserNotFoundException
):
    return JSONResponse(

        status_code = 404,
        content = {

            "detail": exc.message
        }
    )

async def invalid_credentials_handler(
        
    request: Request,
    exc: InvalidCredentialsException
):
    
    return JSONResponse(
        
        status_code = 401,
        content = {
            "detail": exc.message
        }
    )

async def username_already_exists_handler(
        
        request: Request,
        exc: UsernameAlreadyExistsException
):
    return JSONResponse(

        status_code = 400,
        content = {
            "detail": exc.message
        }
    )   

async def email_already_exists_handler(
        
        request: Request,
        exc: EmailAlreadyExistsException
):
    return JSONResponse(

        status_code = 400,
        content = {
            
            "detail": exc.message
        }
    )
