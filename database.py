from sqlmodel import create_engine, SQLModel, Session

# Replace with your Neon database connection URL
DATABASE_URL ="postgresql://neondb_owner:npg_EAZ1rV5wPvMW@ep-shiny-water-a135ra4z-pooler.ap-southeast-1.aws.neon.tech/BLOGI?sslmode=require"

engine = create_engine(DATABASE_URL)

# Function to get DB session
def get_session():
    with Session(engine) as session:
        yield session

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)






