import datetime
import sqlalchemy
from .db_session import SqlAlchemyBase


class User(SqlAlchemyBase):
    __tablename__ = 'users'
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    user_id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    clas = sqlalchemy.Column(sqlalchemy.TEXT)
    prof = sqlalchemy.Column(sqlalchemy.TEXT)
