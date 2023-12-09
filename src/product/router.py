from fastapi import Request, APIRouter, Depends
from sqlalchemy.orm import Session

from src.database import get_async_session

router = APIRouter(
    prefix="/product",
    tags=["Product"]
)


@router.get("/get_product_info")
async def get_product_info(id: int, db: Session = Depends(get_async_session)):
    pass


@router.get("/get_products")
async def get_products(db: Session = Depends(get_async_session)):
    return 123


@router.get("/get_all_users")
async def get_all_users(session: Session = Depends(get_async_session)):
    return "Hello World!"