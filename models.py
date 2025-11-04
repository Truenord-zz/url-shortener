from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class URL(Base):
    pass

# We want the database to have these fields
# id, original_url, new_url, creation_time, views.