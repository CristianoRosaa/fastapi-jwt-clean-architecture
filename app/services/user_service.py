from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.models.user import User

from app.schemas.user import(
    UserCreate
)

from app.repositories import user_repository

from app.exceptions.user_exceptions import(

    UsernameAlreadyExistsException,
    EmailAlreadyExistsException,
    InvalidCredentialsException
)

from app.core.security import(
    
    hash_password,
    
    verify_password,
    
    create_access_token
)

from app.core.logger import logger


def register(
        
        db: Session,

        user: UserCreate
):

    logger.info(
    f"Creating user {user.username}"
)

    existing_user = (
        user_repository.get_by_username(
            db, 
            user.username
        )
    )

    if existing_user:
        
        logger.warning(
            f"Username already exists: {user.username}"
)
        raise UsernameAlreadyExistsException()
    
    existing_email = (
        user_repository.get_by_email(
            db,
            user.email
        )
    )

    if existing_email:
        
        logger.warning(
            f"Email already exists: {user.email}"
        )

        raise EmailAlreadyExistsException()
    
    new_user = User(
        username=user.username,

        email=user.email,

        password=hash_password(
            user.password
        )
    )    

    logger.info(
        
        f"User created successfully: {user.username}"
    )


    return user_repository.create(

        db,

        new_user
    )

def login(
        
        db: Session,
        
        username: str,

        password: str

):
    
    logger.info(

        f"Login attempt: {username}"
    )

    db_user = (
        user_repository.get_by_username(
            
            db,
            username 
        )
    )

    if db_user is None:
        
        logger.warning(
            f"Invalid login for {username}"
        )

        raise InvalidCredentialsException()
    
    if not verify_password(

        password,
        db_user.password

    ):

        logger.warning(
            f"Wrong password for {username}"
        )
        
        raise InvalidCredentialsException()


    access_token = (

        create_access_token(
            data={
                "sub":
                db_user.username
            }
        )
    )

    logger.info(

        f"Login successfully: {username}"

    )

    return{
        "access_token": access_token,
        "token_type": "bearer"
    }

