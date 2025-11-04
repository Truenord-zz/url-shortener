# database address

# get and set methods

# create the engine and give it an address
DATABASE_URL = "sqlite:///./shortener.db"
engine = create_engine(...)

# this will get the seesion running
SessionLocal = sessionmaker(...)

# this builds the tabels
Base.metadata.create_all(bind=engine)

# should open con, do something, close it