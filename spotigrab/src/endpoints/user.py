from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ormtst.src.models import User, UserCreate
from ormtst.src.database import SessionLocal, crud


router = APIRouter(
    tags=['Station attributes'],
    responses={404: {'description': 'Not found'}},
)


def get_db():
    # Dependency
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/users/", response_model=User)
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user.user_id)
    if db_user:
        raise HTTPException(status_code=400, detail="User already registered")
    return crud.create_user(db=db, user=user)


@router.get("/users/", response_model=list[User])
async def read_users(
        skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@router.get("/number-of-users/", response_model=int)
async def number_of_users(db: Session = Depends(get_db)):
    result = crud.get_number_of_users(db)
    return result


@router.get("/users/{user_id}", response_model=User)
async def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
