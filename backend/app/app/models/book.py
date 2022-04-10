from sqlalchemy import Column, Integer, String, Date, Float

from app.db.base_class import Base


class Book(Base):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author = Column(String, index=True)
    publisher = Column(String)
    published_date = Column(Date)
    description = Column(String, nullable=True)
    page_count = Column(Integer, nullable=True)
    avg_rating = Column(Float, nullable=True)
    ratings_count = Column(Integer, nullable=True)
