from typing import List, Any

from app import crud
from app.api import deps
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import schemas

router = APIRouter()


@router.get("/", response_model=List[schemas.Book])
def get_books(
        db: Session = Depends(deps.get_db),
        skip: int = 0,
        limit: int = 100,
) -> Any:
    books = crud.book.get_multi(
        db=db,
        skip=skip,
        limit=limit
    )
    return books


@router.post("/", response_model=schemas.Book)
def create_book(
        *,
        db: Session = Depends(deps.get_db),
        book_in: schemas.BookCreate,
) -> Any:
    """
    Create new book.
    """
    book = crud.book.create(
        db=db,
        obj_in=book_in
    )
    return book


@router.put("/{id}", response_model=schemas.Book)
def update_book(
        *,
        db: Session = Depends(deps.get_db),
        id: int,
        book_in: schemas.BookUpdate,
) -> Any:
    book = crud.book.get(db=db, id=id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    book = crud.book.update(
        db=db,
        db_obj=book,
        obj_in=book_in
    )
    return book


@router.get("/{id}", response_model=schemas.Book)
def read_book(
        *,
        db: Session = Depends(deps.get_db),
        id: int,
) -> Any:
    book = crud.book.get(db=db, id=id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@router.delete("/{id}", response_model=schemas.Book)
def delete_book(
        *,
        db: Session = Depends(deps.get_db),
        id: int
) -> Any:
    book = crud.book.get(db=db, id=id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    book = crud.book.remove(db=db, id=id)
    return book
