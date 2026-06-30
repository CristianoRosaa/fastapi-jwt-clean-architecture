from fastapi import HTTPException, APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import user as models
from app.schemas import user as schemas 

from app.core.security import(
    verify_password,
    create_access_token,
    hash_password
)

from app.core.dependencies import get_current_user

from fastapi.security import OAuth2PasswordRequestForm 

from app.services import user_service


router = APIRouter()


@router.post(
    
    "/register",
    
    response_model=schemas.UserResponse
)

def register(
    
    user: 
    
    schemas.UserCreate,

    db:

    Session = Depends(

        get_db

    )
):
    
    return user_service.register(
        
        db = db,

        user=user 
    )

@router.post("/login")

def login(
    form_data:

    OAuth2PasswordRequestForm = Depends(),

    db:

    Session = Depends(
        get_db
    )
):  
    
    return user_service.login(

        db = db,

        username = form_data.username,

        password = form_data.password
    ) 


@router.get(
    "/profile",
    response_model=schemas.UserResponse
)

def profile(
    current_user: models.User = Depends(
        get_current_user
    )
):
    return current_user


