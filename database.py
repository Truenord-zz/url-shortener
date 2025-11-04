from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base
# database address

# get and set methods

# create the engine and give it an address
DB_ADDRESS = "sqlite:///./shortener.db"
url_engine = create_engine(
    DB_ADDRESS,
    connect_args={"check_same_thread": False}
) # makes it so fastapi can use sqlite, todo concurrency? maybe full scale server-client setup

# this will get the session running
SessionLocal = sessionmaker(
    autoflush=False, # initally lets control when we update db
    bind=url_engine
)

# this builds the tabels, for each object inheriting from base
Base.metadata.create_all(bind=url_engine)

# very barebones, create session, give db con to some caller and then close it
def get_db():
    db = SessionLocal() # init a session
    
    try:
        yield db #lazy yield
    finally: #we gotta close it, always!
        db.close() 
        
