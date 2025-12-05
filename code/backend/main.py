from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path
from sqlmodel import Field, Session, SQLModel, create_engine, select
import uvicorn
from models import *

#TODO:setup the database
#connect svelte to the database
#create (Delete , Modifiy , Create) functions for database
#connect sevelte to do thsose 

DATABASE_URL = "sqlite:///database.db"

engine = create_engine(DATABASE_URL,connect_args={"check_same_thread":False})
SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session
SessionDep = Annotated[Session, Depends(get_session)]


app = FastAPI()


@app.get("/api/get_tasks")
def get_task(session:SessionDep):
    select_tasks = select(TasksDb)
    tasks = session.exec(select_tasks)
    results = tasks.all()
    return results

@app.post("/api/create_task")
def create_task(task:TasksDb,session:SessionDep):
    
    session.add(task)
    session.commit()
    session.refresh(task)
    return task






build_dir = Path(__file__).parent.parent / "frontend" / "build"


app.mount("/_app", StaticFiles(directory=build_dir / "_app"), name="_app")

app.mount("/immutable", StaticFiles(directory=build_dir / "_app" / "immutable"), name="immutable")


#  Fallback to index.html for all other routes (SPA routing)
@app.get("/{full_path:path}")
async def spa_fallback(full_path: str):
    return FileResponse(build_dir / "index.html")

if __name__ == "__main__":
    uvicorn.run("main:app", port=5000, reload=True)
