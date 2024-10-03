from sqlalchemy import String, Column, ForeignKey, Integer, Boolean
from sqlalchemy.orm import relationship

from database import Base

class Artists(Base):
    __table_name__ = "artist_table"
    
    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    song = relationship("Songs", backref='artist')

class Songs(Base):
    __table_name__ = "songs_table"
    
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, index=True)
    popularity = Column(Integer)
    duration_ms = Column(Integer)
    artist_id = Column(Integer, ForeignKey("artist.id"))

class Genres(Base):
    __table__ = "genres_table"

    id = Column(Integer, primary_key=True)
    genre = Column(String)

class Albums(Base):
    __table__ = "albums_table"

    id = Column(Integer, primary_key=True)
    album = Column(String)



    
    

    