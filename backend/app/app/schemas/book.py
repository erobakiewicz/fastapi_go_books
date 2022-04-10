import datetime
from pydantic import BaseModel


class BookBase(BaseModel):
    title: str
    author: str
    publisher: str
    published_date: datetime.date
    description: str
    page_count: int
    avg_rating: float
    ratings_count: int


class BookCreate(BookBase):
    pass


class BookUpdate(BookBase):
    pass


class BookInDBBase(BookBase):
    class Config:
        orm_mode = True


class Book(BookInDBBase):
    pass


class BookInDB(BookInDBBase):
    pass
