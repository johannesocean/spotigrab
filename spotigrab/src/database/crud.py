from sqlalchemy.orm import Session

from ormtst.src.models.user import UserCreate
from ormtst.src.database import models


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.user_id == user_id).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def get_number_of_users(db: Session):
    return db.query(models.User).count()


def create_user(db: Session, user: UserCreate):
    db_user = models.User(
        user_id=user.user_id,
        name=user.name,
        superpower=user.superpower
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
