from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

# We want the database to have these fields
# id, original_url, new_url, creation_time, views.
class URL(Base):
    __tablename__ = "urls" 
    # coloumns for each row: url
    id = Column(Integer, primary_key=True, index=True, nullable=False)
    original_url = Column(String, nullable=False)
    short_url = Column(String, unique=True, index=True, nullable=False)
    creation_time = Column(DateTime, default=datetime.now(datetime.timezone.utc), nullable=False)
    views = Column(Integer, default=0, nullable=False)