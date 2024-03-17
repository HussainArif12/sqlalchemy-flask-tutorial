from db import db
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, relationship

from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from Book import Book
    
#our table will have the name 'author_table'
class Author(db.Model):
    __tablename__  = "author_table"

	# it will have two fields:
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(db.String, nullable=False)
    books: Mapped[List["Book"]] = relationship(back_populates="author")