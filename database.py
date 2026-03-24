import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Load env file
load_dotenv()

#Get database url from environment
db_url= os.getenv("DATABASE_URL") #"postgresql://rama:Kanishka$123456@localhost:5432/fastapi_db"

# Create engine
engine = create_engine(db_url)

#Session
SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)






