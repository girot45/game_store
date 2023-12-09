from fastapi import Request, APIRouter, Depends
from sqlalchemy.orm import Session

from src.database import get_async_session

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.get("/get_all_users")
async def get_all_users(session: Session = Depends(get_async_session)):
    return "Hello World!"


@router.get("/get_user_games")
async def get_user_games(session: Session = Depends(get_async_session)):
    return "Hello World!"


@router.post("/auth/login")
async def login(session: Session = Depends(get_async_session)):
    pass


@router.post("/auth/logout")
async def logout():
    return True


@router.post("/auth/register")
async def register(
        request: Request,
        session: Session = Depends(get_async_session)
):
    return True


@router.post("/top_up_balance")
async def add_balance(session: Session = Depends(get_async_session)):
    return "Hello World!"


@router.post("/debit_by_id")
async def debit_by_id(id:int, session: Session = Depends(get_async_session)):
    return "Hello World!"