from sqlalchemy import Column, Integer, String

from settings import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __repr__(self):
        return "<" + self.__class__.__name__ + str(vars(self)) + ">"
