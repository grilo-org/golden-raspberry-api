from fastapi import FastAPI
from contextlib import asynccontextmanager
from sqlalchemy import inspect

# application
from application.database.sqlite import Base, engine, SessionLocal
from application.database.seeder.seeder import load_data
from application.routes.api import router as routes

@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        # create table
        Base.metadata.create_all(bind=engine)
        db = SessionLocal()
        # populate table
        load_data(db)
        # confirm that table have data
        inspector = inspect(engine)
        print("Tables ready:", inspector.get_table_names())
        # async generator
        yield
    except Exception as e:
        print(f"[Startup] Can't init application: {e}")
        raise
    finally:
        db.close()

# call intance
app = FastAPI(lifespan=lifespan)

# include all routes
app.include_router(routes)