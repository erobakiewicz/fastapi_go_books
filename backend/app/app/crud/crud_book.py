from typing import List

from app.crud.base import CRUDBase
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.models.book import Book
from app.schemas.book import BookCreate, BookUpdate


class CRUDBook(CRUDBase[Book, BookCreate, BookUpdate]):
    def create(self, db: Session, *, obj_in: BookCreate) -> Book:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_all(self, db: Session, *, skip: int = 0, limit: int = 100) -> List[Book]:
        return (
            db.query(self.model).offset(skip).limit(limit).all()
        )

book = CRUDBook(Book)
