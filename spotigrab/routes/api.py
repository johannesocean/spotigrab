from fastapi import APIRouter
from ormtst.src.endpoints import user


router = APIRouter()
router.include_router(user.router)
