from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer,String, Text
from sqlalchemy.orm import declarative_base
from api.database import db


class Video(db.Model):
    __tablename__ = 'videos'
    id:Mapped[int] = mapped_column(Integer, primary_key=True)
    name:Mapped[str] = mapped_column(String, nullable=False)
    description:Mapped[str] = mapped_column(String, nullable=False)