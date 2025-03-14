from sqlmodel import create_engine, SQLModel, Session
import os
# Replace with your Neon database connection URL
DATABASE_URL= os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL is not set in the .env file")


engine = create_engine(DATABASE_URL)

# Function to get DB session
def get_session():
    with Session(engine) as session:
        yield session

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)






