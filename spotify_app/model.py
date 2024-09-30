from sqlalchemy import String, Column, ForeignKey, Integer, Boolean
from sqlalchemy.orm import relationship

from database import Base

class User(Base):
    __table_name__ = "users"
    
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    
    owner = relationship("Item", backref='user')
    

class Item(Base):
    __table_name__ = "items"
    
    id = Column(Integer, primary_key=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))
    