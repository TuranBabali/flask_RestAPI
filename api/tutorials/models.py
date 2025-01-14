from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer,String, Text
from sqlalchemy.orm import declarative_base
from flask_jwt_extended import create_access_token
from datetime import timedelta

from api.database import db


class Video(db.Model):
    __tablename__ = 'videos'
    id:Mapped[int] = mapped_column(Integer, primary_key=True)
    name:Mapped[str] = mapped_column(String, nullable=False)
    description:Mapped[str] = mapped_column(String, nullable=False)

class User(db.Model):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name:Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String,  nullable=False)
    password: Mapped[str] = mapped_column(String, nullable=False)
    # videos = relationship('Video',backref='user',lazy=True)
    videos: Mapped[list["Video"]] = relationship('Video', backref='user', lazy=True) 


    def get_token(self,expire_time=24):
        expire_delta= timedelta(expire_time)
        token= create_access_token(identity=self.id,expires_delta=expire_delta)  
        return token