from typing import Union
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float

# строка подключения
SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# создание движка
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# создаем базовый класс для моделей
Base = declarative_base()
# создаем модель, объекты которой будут храниться в бд


class Person(Base):
    __tablename__ = "people"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    age = Column(Integer, )


class Flower(Base):
    __tablename__ = 'flower'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    price = Column(Float)


# создаем таблицы
Base.metadata.create_all(bind=engine)
