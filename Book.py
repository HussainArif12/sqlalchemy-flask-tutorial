from db import db
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, relationship
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Author import Author
    
class Book(db.Model):
    __tablename__ = "book_table"
    
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    name: Mapped[str] = mapped_column(db.String,nullable=False)
    # here, we are adding another field so that each book in the database
	# can link to its author
    author_id: Mapped[int] = mapped_column(db.ForeignKey("author_table.id"))
    author: Mapped["Author"] = relationship(back_populates="books")