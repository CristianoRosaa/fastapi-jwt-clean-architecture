from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import user as models

from app.core.security import(
    oauth2_scheme,
    verify_token
)

def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):
    
    username = verify_token(token)

    if username is None:
        raise HTTPException(
            status_code=401,
            detail="invalid credentials"
        )
    
    user = db.query(models.User).filter(
        models.User.username == username
    ).first()

    if user is None:
        raise HTTPException(
            status_code=401,
            detail="User not found"
        )
    
    return user
