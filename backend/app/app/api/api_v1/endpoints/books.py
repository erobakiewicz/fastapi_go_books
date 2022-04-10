from typing import List, Any

from app import crud
from app.api import deps
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import schemas

router = APIRouter()

@router.get("/", response_model=List[schemas.Book])
def get_books(
        db: Session = Depends(deps.get_db),
        skip: int = 0,
        limit: int = 100,
) -> Any:
    books = crud.book.get_all(
        db=db,
        skip=skip,
        limit=limit
    )
    return books
